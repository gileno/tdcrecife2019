import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class VivarealSpider(CrawlSpider):   
    name = 'vivareal_crawl'
    start_urls = ['https://www.vivareal.com.br/venda/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/']
    rules = (
        Rule(
            LinkExtractor(allow='/venda/pernambuco/recife/bairros/boa-viagem/apartamento_residencial/')
        ),
        Rule(
            LinkExtractor(
                allow='/imovel/',
            ), callback='parse_imovel'
        )
    )
    def parse_imovel(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first()
        }

