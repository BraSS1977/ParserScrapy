import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    # Настройки для экспорта в CSV
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'divan_svet.csv',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_FIELDS': ['name', 'price', 'link'],
    }


    def parse(self, response):
        svets = response.css('div._Ud0k')

        for svet in svets:
            yield {
                "name": svet.css("div.lsooF span::text").get(),
                "price": svet.css("div.pY3d2 span::text").get(),
                "link": svet.css("a::attr(href)").get()
            }
