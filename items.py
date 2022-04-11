# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join, Identity
from w3lib.html import remove_tags

# def extract_from_html(string):
#     regex = '(?<=\<b>)(.*?)(?=<)'
#     str_list = re.findall(regex, string)
#     return str_list
def clean_title(str):
    return str.replace("śląskie,", "").strip().split(", ", 1)

def clean_string(string):
    return (string
            .strip()
            .replace(" ", "-")
            .replace("m²", "m2")
            .split('-')
            )
def clean_price(price):
    import re
    return re.sub('\D', '', price)


class RealestatescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(input_processor=MapCompose(remove_tags, clean_title),
                        output_processor=Identity())

    price = scrapy.Field(input_processor=MapCompose(remove_tags, clean_price),
                         output_processor=TakeFirst())
    ro_sp_fl = scrapy.Field(input_processor=MapCompose(remove_tags, clean_string),
                            output_processor=Identity())
    link = scrapy.Field()
