# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClassmatesItem(scrapy.Item):
    # define the fields for your item here like:
    
    course_code = scrapy.Field()
    course_name = scrapy.Field()
