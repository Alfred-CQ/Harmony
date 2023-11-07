import scrapy
from wikipedia_scraper.items import WikipediaScraperItem

def link_is_useful(link):
    if link[:6] != '/wiki/':
        return False
    if ':' in link:
        return False
    return True

class WikipediaSpiderSpider(scrapy.Spider):
    name = "wikipedia_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Big_data"]

    def parse(self, response):
        item = WikipediaScraperItem()
        item['title'] = response.xpath('//*[@id="firstHeading"]/span/text()').get()
        item['content'] = ' '.join(response.css('p::text').getall())
        item['links'] = response.css('a::attr(href)').getall()

        yield item

        for link in item['links']:
            if link_is_useful(link):
                print("------>", link)
                next_page = response.urljoin(link)
                yield response.follow(next_page, callback=self.parse)
    
    def spider_closed(self, spider, reason):
        self.log(f'Spider {spider.name} has been closed due to next reason: {reason}')