import json
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_URL = "https://api.linkedin.com/rest/posts"


def load_calendar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_calendar(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    calendar_path = "content/linkedin-posts.json"
    data = load_calendar(calendar_path)
    now = datetime.now(ZoneInfo(data.get("timezone", "Europe/Lisbon")))
    today = now.date().isoformat()
    current_time = now.strftime("%H:%M")

    due = [p for p in data["posts"] if p.get("status") == "APPROVED" and p.get("publish_date") == today and p.get("publish_time") <= current_time and not p.get("linkedin_post_id")]
    if not due:
        print("No approved LinkedIn company page post is due.")
        return 0

    if len(due) > 1:
        print("More than one approved post is due. Refusing to publish automatically.", file=sys.stderr)
        return 1

    post = due[0]
    token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
    organization_urn = os.environ.get("LINKEDIN_ORGANIZATION_URN")
    if not token or not organization_urn:
        print("Missing LinkedIn credentials. Set LINKEDIN_ACCESS_TOKEN and LINKEDIN_ORGANIZATION_URN.", file=sys.stderr)
        return 1

    payload = {
        "author": organization_urn,
        "commentary": post["text"],
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }

    request = Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Linkedin-Version": os.environ.get("LINKEDIN_VERSION", "202602"),
            "X-Restli-Protocol-Version": "2.0.0"
        },
        method="POST"
    )

    try:
        with urlopen(request, timeout=30) as response:
            post_id = response.headers.get("x-restli-id", "")
            body = response.read().decode("utf-8")
    except HTTPError as error:
        print(error.read().decode("utf-8"), file=sys.stderr)
        return 1

    post["status"] = "PUBLISHED"
    post["published_at"] = now.isoformat()
    post["linkedin_post_id"] = post_id or body
    save_calendar(calendar_path, data)
    print(f"Published {post['id']} successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
