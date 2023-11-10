import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from wikipedia_scraper.spiders.wikipedia_spider import WikipediaSpiderSpider

def run(settings, spider):
    process = CrawlerProcess(settings)
    process.crawl(spider)
    process.start()

def run_wikipedia_spider():
    settings = get_project_settings()
    settings.update({
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'output.json',
        'CLOSESPIDER_PAGECOUNT': 100,
    })

    run(settings, WikipediaSpiderSpider)

#run_wikipedia_spider()
