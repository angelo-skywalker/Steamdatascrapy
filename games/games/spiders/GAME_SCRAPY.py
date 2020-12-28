import scrapy


class GameSpider(scrapy.Spider):
    name = 'games'

    start_urls = ['https://play.eslgaming.com/games']

    def parse(self, response):

       page = response.css('.gamespage').getall()
       filename = 'games.html'
       with open(filename, 'wb') as g:
           g.write(response.body)










