# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass


@dataclass
class AwsInfringementItem:
    item_name: str
    product_description: str
    bullet_point1: str
    bullet_point2: str
    bullet_point3: str
    bullet_point4: str
    bullet_point5: str
