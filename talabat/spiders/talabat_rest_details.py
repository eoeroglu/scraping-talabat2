import scrapy
import json
from scrapy import Request

class Talabat(scrapy.Spider):
    name = 'talabat_restdetails'

    start_urls = [
        'https://www.talabat.com/nextApi/customer?countryId=4'
    ]

    def start_requests(self):
        requests = []
        for item in self.start_urls:
            requests.append(Request(url=item, headers={'Referer':'https://www.talabat.com/uae/pizza-hut'}))
        return requests 

    def parse(self, response):
        jres = json.loads(response.text)
        for item in jres['result']['mostSellingItemsRestaurant']:
            yield {
                'id': item['id'],
                'name': item['rna'],
                'cuisine': item['cs']
            }