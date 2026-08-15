import os
import requests
import json

session = os.environ["LEETCODE_SESSION"]
csrf = os.environ["LEETCODE_CSRF_TOKEN"]

cookies = {
    "LEETCODE_SESSION": session,
    "csrftoken": csrf,
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/",
}

url = "https://leetcode.com/api/submissions/?offset=0&limit=20"

response = requests.get(url, cookies=cookies, headers=headers)
response.raise_for_status()

data = response.json()

for submission in data.get("submissions_dump", []):
    if submission.get("status_display") == "Accepted":
        print("TITLE:", submission.get("title"))
        print("QUESTION ID:", submission.get("question_id"))
        print("LANGUAGE:", submission.get("lang"))
        print("STATUS:", submission.get("status_display"))
        print("---")