import os
import re
import html
from pathlib import Path

import requests
from openai import OpenAI


# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)


# ============================================================
# LEETCODE CONFIG
# ============================================================

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

cookies = {
    "LEETCODE_SESSION": SESSION,
    "csrftoken": CSRF,
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/",
    "Content-Type": "application/json",
}


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


def clean_leetcode_html(content):
    """
    Convert LeetCode's HTML problem description
    into reasonably readable Markdown.
    """

    if not content:
        return ""

    content = html.unescape(content)

    # Normalize line breaks
    content = re.sub(r"<br\s*/?>", "\n", content, flags=re.I)

    # Headings
    content = re.sub(
        r"<h[1-6][^>]*>(.*?)</h[1-6]>",
        r"\n\1\n",
        content,
        flags=re.I | re.S
    )

    # Paragraphs
    content = re.sub(
        r"<p[^>]*>(.*?)</p>",
        r"\n\1\n",
        content,
        flags=re.I | re.S
    )

    # Bold
    content = re.sub(
        r"<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>",
        r"**\1**",
        content,
        flags=re.I | re.S
    )

    # Italic
    content = re.sub(
        r"<(?:em|i)[^>]*>(.*?)</(?:em|i)>",
        r"*\1*",
        content,
        flags=re.I | re.S
    )

    # Inline code
    content = re.sub(
        r"<code[^>]*>(.*?)</code>",
        r"`\1`",
        content,
        flags=re.I | re.S
    )

    # List items
    content = re.sub(
        r"<li[^>]*>(.*?)</li>",
        r"\n- \1",
        content,
        flags=re.I | re.S
    )

    # Preformatted code/examples
    content = re.sub(
        r"<pre[^>]*>(.*?)</pre>",
        r"\n```\n\1\n```\n",
        content,
        flags=re.I | re.S
    )

    # Remove remaining HTML tags
    content = re.sub(
        r"<[^>]+>",
        "",
        content
    )

    # Decode entities again
    content = html.unescape(content)

    # Clean excessive whitespace
    content = re.sub(
        r"\n\s*\n\s*\n+",
        "\n\n",
        content
    )

    return content.strip()


# ============================================================
# GRAPHQL REQUEST
# ============================================================

def graphql_request(query, variables):
    response = requests.post(
        LEETCODE_GRAPHQL,
        json={
            "query": query,
            "variables": variables,
        },
        cookies=cookies,
        headers=headers,
        timeout=30,
    )

    print(f"GraphQL status: {response.status_code}")

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        print("GraphQL errors:")
        print(data["errors"])
        return None

    return data.get("data")


# ============================================================
# GET RECENT SUBMISSIONS
# ============================================================

def get_submissions():

    query = """
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

    data = graphql_request(
        query,
        {
            "offset": 0,
            "limit": 50,
        }
    )

    if not data:
        return []

    submission_list = data.get(
        "submissionList",
        {}
    )

    return submission_list.get(
        "submissions",
        []
    )


# ============================================================
# GET SUBMISSION CODE
# ============================================================

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

    data = graphql_request(
        query,
        {
            "submissionId": int(submission_id)
        }
    )

    if not data:
        return None

    return data.get(
        "submissionDetails"
    )


# ============================================================
# GET QUESTION METADATA + DESCRIPTION
# ============================================================

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

    data = graphql_request(
        query,
        {
            "titleSlug": title_slug
        }
    )

    if not data:
        return None

    return data.get(
        "question"
    )


# ============================================================
# GENERATE README WITH AI
# ============================================================

def generate_readme(
    title,
    problem_id,
    difficulty,
    language,
    tags,
    description,
    code
):

    prompt = f"""
You are creating a README.md for a student's LeetCode repository.

Create a clean, useful Markdown README.

Problem:
{title}

Problem Number:
{problem_id}

Difficulty:
{difficulty}

Language:
{language}

Topics:
{", ".join(tags)}

Original LeetCode Problem Description:
{description}

Student's Accepted Solution:

```{language}
{code}