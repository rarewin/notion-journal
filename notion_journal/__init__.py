import os
import re
from datetime import datetime

from pprint import pprint
from notion_client import Client


def main(token, database_id):

    notion = Client(auth=token)

    reg_daily_page = re.compile(r"^\d{4}-\d{2}-\d{2}")

    daily_data = []

    for e in notion.databases.query(database_id).get("results"):
        if e["object"] == "page" and reg_daily_page.match(
            e["properties"]["Name"]["title"][0]["plain_text"]
        ):
            daily_data.append(
                {
                    "id": e["id"],
                    "date": datetime.fromisoformat(
                        e["properties"]["Date"]["date"]["start"]
                    ),
                    "title": e["properties"]["Name"]["title"][0]["plain_text"],
                }
            )

    daily_data.sort(key=lambda e: e["date"])

    pprint(daily_data)
    # daily_data.sort(key=lambda e: e["properties"]["Date"]["date"]["start"])

    # 指定日(or 本日)よりも古い記事のうちで、一番新しい記事を取得する
    # タイトルも気をつけるか

    creation_date = datetime.today()

    # previous_data = filter(lambda e: )


if __name__ == "__main__":

    token = os.environ.get("NOTION_API_TOKEN")
    database_id = os.environ.get("DATABASE_ID")

    main(token, database_id)
