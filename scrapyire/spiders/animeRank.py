import scrapy
from typing import Any
from scrapy.http import Response


class AnimerankSpider(scrapy.Spider):
    name = "animeRank"
    allowed_domains = ["www.douban.com"]
    start_urls = ["https://www.douban.com/doulist/45955373/"]

    def parse(self, response: Response, **kwargs: Any):
        print("网页内容:", response.text)
        pass
