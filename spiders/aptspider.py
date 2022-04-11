import scrapy
from realestatescrapy.items import RealestatescrapyItem
from scrapy.loader import ItemLoader

class AptSpider(scrapy.Spider):
    name = 'apart'
    start_urls = ['https://www.morizon.pl/mieszkania/gliwice/?page=1',
                  'https://www.morizon.pl/mieszkania/rybnik/?page=1']

    def parse(self, response):
        for products in response.css('div.row-content.row-property.single-result.mz-card.mz-card_no-animation.mz-card--listing'): #'div.row.row--property-list'
            l = ItemLoader(item=RealestatescrapyItem(), selector=products)

            l.add_css('name', 'h2.single-result__title')
            l.add_css('price', 'p.single-result__price')
            l.add_css('ro_sp_fl', 'div.info-description.single-result__info')
            l.add_css('link', 'a.property_link.property-url::attr(href)')

            yield l.load_item()


        next_page = response.css('a.mz-pagination-number__btn.mz-pagination-number__btn--next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, dont_filter=True)