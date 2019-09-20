""" quote scrapy """
import scrapy
from scrapyTutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    """
    * name: identifies the Spider.
    * start_requests(): must return an iterable of Requests
      which the Spider will begin to crawl from.
    * parse(): a method that will be called to handle the response
      downloader for each of the request made.
    """

    name = "quotes"

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuotesItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('small.author::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
