# aws-infringement

## Setup

```shell
poetry install

```

## Run the spider

```
poetry shell
scrapy runspider aws_infringement/aws_infringement/spiders/aws_excel_spider.py -a excel_path='./excels/example.xlsx' -o result.csv
```
