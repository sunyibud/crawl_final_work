import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github'
    # allowed_domains = ['www.xx']
    start_urls = ['https://github.com/explore']


    def parse_get_topics(self, response):
        div_lst = response.xpath('//*[@id="js-pjax-container"]/div[4]/div[1]/div/div')
        for div in div_lst:
            dic = {}
            dic['href'] = r'https://github.com' + div.xpath('./a[1]/@href').extract_first().strip()
            dic['name'] = div.xpath('./a[1]/div/div/p[1]/text()').extract_first().strip()
            dic['describe'] = div.xpath('./a[1]/div/div/p[2]/text()').extract_first().strip()
            print(dic)
            break

    def parse(self, response):
        kinds_lst = response.xpath('//*[@id="js-pjax-container"]/div[1]/nav/div/a/@href').extract()
        print(kinds_lst)

