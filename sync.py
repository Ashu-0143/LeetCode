import os
import re
import requests
from pathlib import Path

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]

BASE_URL = "https://leetcode.com"

cookies = {
    "LEETCODE_SESSION": SESSION,
    "csrftoken": CSRF,
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/",
}

# Get recent submissions
url = f"{BASE_URL}/api/submissions/?offset=0&limit=20"

response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
)

response.raise_for_status()

data = response.json()

for submission in data.get("submissions_dump", []):

    # Only save accepted submissions
    if submission.get("status_display") != "Accepted":
        continue

    question_id = submission["question_id"]
    title = submission["title"]
    language = submission["lang"]
    code = submission["code"]

    # Get problem information
    graphql_url = f"{BASE_URL}/graphql"

    query = {
        "query": """
        query questionData($questionId: String!) {
            question(questionId: $questionId) {
                questionFrontendId
                title
                difficulty
            }
        }
        """,
        "variables": {
            "questionId": str(question_id)
        }
    }

    problem_response = requests.post(
        graphql_url,
        json=query,
        cookies=cookies,
        headers=headers,
    )

    if problem_response.status_code != 200:
        print(f"Could not get difficulty for {title}")
        continue

    problem_data = problem_response.json()

    question = problem_data.get("data", {}).get("question")

    if not question:
        print(f"Could not find problem: {title}")
        continue

    difficulty = question["difficulty"]

    # Clean title for folder name
    safe_title = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")

    problem_id = str(question["questionFrontendId"]).zfill(4)

    folder = Path(difficulty) / f"{problem_id}-{safe_title}"
    folder.mkdir(parents=True, exist_ok=True)

    # File extension
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

    print(f"Saved: {output_file}")