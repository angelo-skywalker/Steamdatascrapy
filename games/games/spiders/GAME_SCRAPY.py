import scrapy


class GameSpider(scrapy.Spider):
    name = 'games'

    start_urls = ['https://play.eslgaming.com/games']

    def parse(self, response):

       for games in response.css('.gamespage'):
           yield {
               'image' : response.xpath("//div[2]/div/div/a/img").getall(),  #extract the images from the ESL Gamepage
               'title' : response.xpath("//div[2]/div/div/a/p").getall(),  #extract the game title
           }










