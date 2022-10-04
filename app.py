from __future__ import annotations

from html.parser import HTMLParser

import requests
from fake_useragent import UserAgent


class CustomParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags_all = []
        self.tags_with_attribute = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags_all.append(tag)
        if attrs:
            self.tags_with_attribute.append(tag)

    def handle_endtag(self, tag: str) -> None:
        self.tags_all.append(tag)


def get_tags_amount() -> None:
    parser = CustomParser()
    ua = UserAgent()
    url = "https://jetlend.ru/"
    headers = {"User-Agent": ua.random}

    html_response = requests.get(url, headers=headers)
    parser.feed(html_response.text)

    print(f"Total amount of tags is { len(parser.tags_all)}")
    print(f"Total amount of tags with attributes is { len(parser.tags_with_attribute)}")


if __name__ == "__main__":
    get_tags_amount()
