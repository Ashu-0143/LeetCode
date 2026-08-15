import os
import re
import requests
from pathlib import Path

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]

cookies = {
    "LEETCODE_SESSION": SESSION,
    "csrftoken": CSRF,
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/",
    "Content-Type": "application/json",
}

# Get recent submissions
response = requests.get(
    "https://leetcode.com/api/submissions/?offset=0&limit=20",
    cookies=cookies,
    headers=headers,
)

response.raise_for_status()

submissions = response.json().get("submissions_dump", [])

processed = set()

for submission in submissions:

    if submission.get("status_display") != "Accepted":
        continue

    question_id = submission["question_id"]
    title = submission["title"]
    language = submission["lang"]
    code = submission["code"]

    # Avoid duplicate submissions of the same problem
    if question_id in processed:
        continue

    processed.add(question_id)

    # Convert title to a LeetCode slug
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")

    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "titleSlug": slug
        }
    }

    result = requests.post(
        "https://leetcode.com/graphql",
        json=payload,
        cookies=cookies,
        headers=headers,
    )

    print(f"Checking: {title} ({slug})")
    print(f"GraphQL status: {result.status_code}")

    if result.status_code != 200:
        print(f"Failed lookup: {title}")
        continue

    question = result.json().get("data", {}).get("question")

    if not question:
        print(f"Could not find metadata for: {title}")
        continue

    difficulty = question["difficulty"]

    problem_id = str(question["questionFrontendId"]).zfill(4)

    safe_title = re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        title.lower()
    ).strip("-")

    folder = Path(difficulty) / f"{problem_id}-{safe_title}"
    folder.mkdir(parents=True, exist_ok=True)

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
    }

    extension = extensions.get(language.lower(), "txt")

    output_file = folder / f"solution.{extension}"

    if output_file.exists():
        print(f"Already exists: {output_file}")
        continue

    output_file.write_text(code, encoding="utf-8")

    print(f"SUCCESS: {output_file}")