import scrapy

class VivaRealSpider(scrapy.Spider):

    name = 'vivareal'
    start_urls = ['https://www.vivareal.com.br/venda/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/']

    def parse(self, response):
        for item in response.xpath("//div[contains(@class, 'results-list')]/div"):
            yield {
                'title': item.xpath(".//h2/a/text()").extract_first().strip()
            }
