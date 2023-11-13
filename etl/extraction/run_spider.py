import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from etl.extraction.wikipedia_scraper import WikipediaSpiderSpider


def run(settings, spider):
    process = CrawlerProcess(settings)
    process.crawl(spider)
    process.start()


def run_wikipedia_spider():
    settings = get_project_settings()
    settings.update(
        {
            "FEED_FORMAT": "json",
            "FEED_URI": "data/wikipedia_extraction.json",
            "CLOSESPIDER_PAGECOUNT": 100,
        }
    )

    run(settings, WikipediaSpiderSpider)
