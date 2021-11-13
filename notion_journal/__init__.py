import os
import re
from datetime import datetime

from pprint import pprint
from notion_client import Client


def main(token, database_id):

    notion = Client(auth=token)

    reg_daily_page = re.compile(r"^\d{4}-\d{2}-\d{2}")

    daily_data = []

    today = datetime.today()

    creation_date = datetime(today.year, today.month, today.day)

    pprint(creation_date)

    for e in notion.databases.query(database_id).get("results"):

        if not "Date" in e["properties"]:
            # pprint(e["properties"])
            continue

        entry_date = datetime.fromisoformat(e["properties"]["Date"]["date"]["start"])

        if not "title" in e["properties"]["Name"]:
            # pprint(e["properties"]["Name"])
            continue

        if (
            e["object"] == "page"
            and reg_daily_page.match(e["properties"]["Name"]["title"][0]["plain_text"])
            and entry_date < creation_date
        ):
            daily_data.append(
                {
                    "id": e["id"],
                    "date": entry_date,
                    "title": e["properties"]["Name"]["title"][0]["plain_text"],
                }
            )

    daily_data.sort(key=lambda e: e["date"])

    # pprint(daily_data)
    # daily_data.sort(key=lambda e: e["properties"]["Date"]["date"]["start"])

    # 指定日(or 本日)よりも古い記事のうちで、一番新しい記事を取得する
    # タイトルも気をつけるか

    # previous_data = list(filter(lambda e: e["date"] <= creation_date, daily_data))

    # pprint(previous_data)

    if len(daily_data) == 0:
        return

    latest = daily_data[-1]

    pprint(latest)

    latest_page = notion.pages.retrieve(latest["id"])

    # pprint(latest_page["properties"]["Property"])
    # pprint(latest_page)

    # synced blockは、まだ未サポートかよぉ……
    pprint(notion.blocks.children.list(latest["id"])["results"])
    # pprint(notion.blocks.children.list(latest["id"])["results"][2])


if __name__ == "__main__":

    token = os.environ.get("NOTION_API_TOKEN")
    database_id = os.environ.get("DATABASE_ID")

    if not token or not database_id:
        print("set NOTION_API_TOKEN & DATABASE_ID")
    else:
        main(token, database_id)
