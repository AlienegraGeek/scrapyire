import scrapy
from typing import Any
from scrapy.http import Response

class EvmSpider(scrapy.Spider):
    name = "evm"
    allowed_domains = ["evm.ink"]
    start_urls = ["https://evm.ink/address/0xf6372ef94026f71e5e48f0ff2ff5ceb06fdff303"]

    def parse(self, response: Response, **kwargs: Any):
        print("网页内容:", response.text)
        pass
