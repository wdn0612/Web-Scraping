import scrapy


class QuotesSpider(scrapy.Spider):
    name = "property_guru"

    def start_requests(self):
        urls = [
            "https://www.propertyguru.com.sg/property-for-rent?market=residential&listing_type=rent&MRT_STATIONS[]=" + "EW19"
        ]
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        page = 1
        filename = f'property-guru-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
