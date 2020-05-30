import scrapy
import pandas as pd

df=pd.read_csv("/Users/hua/Documents/Uconn/Class/Semester2/3. Predictive Modeling/Project/OnlineNewsPopularity/OnlineNewsPopularity.csv",delim_whitespace=False)

url = df['url']

class QuotesSpider(scrapy.Spider):
    name = "getkeys"
    start_urls = url.values.tolist()
    '''
    def start_requests(self):
        urls = [
            'https://mashable.com/2013/01/07/apple-40-billion-app-downloads/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    ''' 

    def parse(self, response):
        for quote in response.css('h1.title'):
            yield {
                'url':response.url,
                'Title': quote.css('h1.title::text').extract_first(),
                'keyword' :response.xpath("//meta[@name='keywords']/@content")[0].extract(),
                'description':response.xpath("//meta[@name='description']/@content")[0].extract(),
                'parsely-metadata' :response.xpath("//meta[@name='parsely-metadata']/@content")[0].extract(),
                'json': response.xpath("//script[@type='application/ld+json']")[0].extract(),
            }
            