import os
import requests

session = os.environ["LEETCODE_SESSION"]
csrf = os.environ["LEETCODE_CSRF_TOKEN"]

url = "https://leetcode.com/api/submissions/?offset=0&limit=20"

cookies = {
    "LEETCODE_SESSION": session,
    "csrftoken": csrf
}

response = requests.get(url, cookies=cookies)

print("Status:", response.status_code)
print(response.text[:1000])