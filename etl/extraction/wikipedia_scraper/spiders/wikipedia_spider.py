import scrapy
from etl.extraction.wikipedia_scraper import WikipediaScraperItem


def link_is_useful(link, cur_url):
    if link[:6] != "/wiki/":
        return False
    if ":" in link:
        return False
    if "identifier" in link:
        return False
    if "/wiki/Main_Page" == link:
        return False
    if cur_url == "https://en.wikipedia.org" + link:
        return False
    return True


scraped_urls = []


class WikipediaSpiderSpider(scrapy.Spider):
    name = "wikipedia_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Big_data"]

    def parse(self, response):
        item = WikipediaScraperItem()
        item["title"] = response.xpath('//*[@id="firstHeading"]/span/text()').get()
        item["title"] = (
            response.xpath('//*[@id="firstHeading"]/i').get()
            if not item["title"]
            else item["title"]
        )
        item["content"] = " ".join(response.css("p::text").getall())
        item["current_link"] = response.url
        item["links"] = response.css("a::attr(href)").getall()
        item["links"] = [
            link for link in item["links"] if link_is_useful(link, response.url)
        ]

        all_as = response.css("p a::text").getall()
        all_as = [a for a in all_as if "[" not in a]
        all_as = " ".join(all_as)

        all_bs = response.css("p b::text").getall()
        all_bs = [b for b in all_bs if "[" not in b]
        all_bs = " ".join(all_bs)

        item["content"] += all_as + " " + all_bs

        yield item

        for link in item["links"]:
            if link in scraped_urls:
                continue
            scraped_urls.append(link)
            next_page = response.urljoin(link)
            yield response.follow(next_page, callback=self.parse)

    def spider_closed(self, spider, reason):
        self.log(f"Spider {spider.name} has been closed due to next reason: {reason}")
