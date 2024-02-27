from scrapy import Spider, Request
from os.path import abspath
from openpyxl import load_workbook
from loguru import logger


class AwsExcelSpider(Spider):
    name = "aws_excel_spider"
    allowed_domains = ["aws.amazon.com"]

    def __init__(self, excel_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = "https://www.amazon.it/gp/product/{}"
        file_path = abspath(excel_path)
        logger.debug(f"file_path: {file_path}")
        self.wb = load_workbook(filename=file_path)
        self.sheet = self.wb["Vorlage"]

    def start_requests(self):
        product_ids = self.sheet["E"]
        for row in product_ids[2:]:
            logger.debug(row.value)
            yield Request(url=self.base_url.format(row.value), callback=self.parse)

    def parse(self, response):
        title = (
            response.xpath("//span[@id='productTitle']/text()").extract_first().strip()
        )
        bullets = response.xpath("//div[@id='feature-bullets']/ul/li/span/text()")
        features = [b.get().strip() for b in bullets]
        description_list = response.xpath(
            "//div[@id='productDescription_feature_div']/div[@id='productDescription']/p/span/text()"
        )
        description = "".join([d.get() for d in description_list])
        result = {
            "item_name": title,
            "product_description": description,
        }
        result.update({"bullet_point" + str(i + 1): features[i] for i in range(5)})
        yield result
