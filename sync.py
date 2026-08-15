import os
import re
from pathlib import Path

import requests
import html2text
from openai import OpenAI


# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)


# ============================================================
# LEETCODE SESSION
# ============================================================

cookies = {
    "LEETCODE_SESSION": SESSION,
    "csrftoken": CSRF,
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/",
    "Content-Type": "application/json",
    "x-csrftoken": CSRF,
}


# ============================================================
# HTML -> MARKDOWN CONVERTER
# ============================================================

html_converter = html2text.HTML2Text()
html_converter.body_width = 0
html_converter.ignore_links = False
html_converter.ignore_images = False


def html_to_markdown(html_content):
    if not html_content:
        return ""
    return html_converter.handle(html_content).strip()


# ============================================================
# GET RECENT SUBMISSIONS
# ============================================================

submission_query = """
query submissionList($offset: Int!, $limit: Int!) {
    submissionList(offset: $offset, limit: $limit) {
        submissions {
            id
            title
            titleSlug
            statusDisplay
            lang
        }
        hasNext
    }
}
"""

payload = {
    "query": submission_query,
    "variables": {
        "offset": 0,
        "limit": 50
    }
}

response = requests.post(
    "https://leetcode.com/graphql",
    json=payload,
    cookies=cookies,
    headers=headers,
    timeout=30,
)

response.raise_for_status()

data = response.json()

if "errors" in data:
    print("LeetCode GraphQL error:")
    print(data["errors"])
    raise SystemExit(1)

submission_data = (
    data
    .get("data", {})
    .get("submissionList", {})
)

submissions = submission_data.get("submissions", [])

print(f"Found {len(submissions)} recent submissions.")


# ============================================================
# LANGUAGE EXTENSIONS
# ============================================================

extensions = {
    "c": "c",
    "cpp": "cpp",
    "java": "java",
    "python": "py",
    "python3": "py",
    "javascript": "js",
    "typescript": "ts",
    "csharp": "cs",
    "kotlin": "kt",
    "rust": "rs",
    "go": "go",
    "swift": "swift",
    "php": "php",
}


# ============================================================
# HELPERS
# ============================================================

def slugify(text):
    return re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        text.lower()
    ).strip("-")


def get_submission_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            lang
            runtime
            memory
            timestamp
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "submissionId": int(submission_id)
        }
    }

    response = requests.post(
        "https://leetcode.com/graphql",
        json=payload,
        cookies=cookies,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        print("Could not get submission code:")
        print(data["errors"])
        return None

    return (
        data
        .get("data", {})
        .get("submissionDetails")
    )


def get_question_metadata(title_slug):
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            content
            topicTags {
                name
            }
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "titleSlug": title_slug
        }
    }

    response = requests.post(
        "https://leetcode.com/graphql",
        json=payload,
        cookies=cookies,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        print("Metadata error:")
        print(data["errors"])
        return None

    return (
        data
        .get("data", {})
        .get("question")
    )


def generate_ai_summary(title, problem_id, difficulty, language, tags, description_md, code):
    prompt = f"""You are analyzing a student's accepted LeetCode solution.

Write a short "Approach" section (3-6 sentences, plain prose, no headers)
explaining the technique used in the code below and its time/space complexity.
Do not repeat the problem statement. Do not include the code itself.

Problem: {title} ({problem_id}, {difficulty})
Topics: {", ".join(tags)}
Language: {language}

Problem description:
{description_md}

Student's submitted code:
```{language}
{code}
```
"""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return completion.choices[0].message.content.strip()


def build_readme(title, problem_id, difficulty, language, tags, description_md, ai_summary, title_slug):
    tag_line = ", ".join(tags) if tags else "—"
    extension = extensions.get(language.lower(), "txt")

    return f"""# {problem_id}. {title}

**Difficulty:** {difficulty}
**Topics:** {tag_line}
**Link:** https://leetcode.com/problems/{title_slug}/

## Problem

{description_md}

## Approach

{ai_summary}

## Solution

See [`solution.{extension}`](./solution.{extension})
"""


# ============================================================
# PROCESS SUBMISSIONS
# ============================================================

processed_slugs = set()

for submission in submissions:

    if submission.get("statusDisplay") != "Accepted":
        continue

    title = submission["title"]
    title_slug = submission["titleSlug"]
    language = submission["lang"]
    submission_id = submission["id"]

    # Dedupe on the *problem*, not the submission — a problem can
    # appear multiple times in recent submissions if resubmitted.
    if title_slug in processed_slugs:
        continue

    processed_slugs.add(title_slug)

    print()
    print("=" * 60)
    print(f"Problem: {title}")
    print(f"Slug: {title_slug}")
    print(f"Language: {language}")

    # --------------------------------------------------------
    # GET QUESTION METADATA (needed for folder path either way)
    # --------------------------------------------------------

    question = get_question_metadata(title_slug)

    if not question:
        print("Could not find question metadata.")
        continue

    difficulty = question["difficulty"]
    problem_id = str(question["questionFrontendId"]).zfill(4)
    tags = [tag["name"] for tag in question.get("topicTags", [])]
    description_md = html_to_markdown(question.get("content"))

    print(f"Problem ID: {problem_id}")
    print(f"Difficulty: {difficulty}")
    print(f"Topics: {', '.join(tags)}")

    safe_title = slugify(title)
    folder = Path(difficulty) / f"{problem_id}-{safe_title}"
    folder.mkdir(parents=True, exist_ok=True)

    extension = extensions.get(language.lower(), "txt")
    solution_file = folder / f"solution.{extension}"
    readme_file = folder / "README.md"

    solution_written = False
    code = None

    # --------------------------------------------------------
    # SAVE SOLUTION (only fetch code if we actually need it)
    # --------------------------------------------------------

    if not solution_file.exists():
        details = get_submission_code(submission_id)

        if not details or not details.get("code"):
            print("Could not retrieve submission code.")
            continue

        code = details["code"]
        solution_file.write_text(code, encoding="utf-8")
        solution_written = True
        print(f"Saved solution: {solution_file}")
    else:
        print(f"Solution already exists: {solution_file}")

    # --------------------------------------------------------
    # README
    # --------------------------------------------------------

    if readme_file.exists():
        print(f"README already exists: {readme_file}")
        continue

    # We need the code for the AI summary even if the solution
    # file already existed from a previous run.
    if code is None:
        code = solution_file.read_text(encoding="utf-8")

    try:
        ai_summary = generate_ai_summary(
            title, problem_id, difficulty, language, tags, description_md, code
        )
    except Exception as e:
        print(f"AI summary failed, falling back to placeholder: {e}")
        ai_summary = "_(AI summary unavailable for this run.)_"

    readme_content = build_readme(
        title, problem_id, difficulty, language, tags,
        description_md, ai_summary, title_slug,
    )

    readme_file.write_text(readme_content, encoding="utf-8")
    print(f"Saved README: {readme_file}")

print()
print("Done.")