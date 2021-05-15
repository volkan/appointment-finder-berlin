import scrapy
import http.client, urllib
from scrapy.utils.project import get_project_settings

class BerlinAnmeldungSpider(scrapy.Spider):
    name = 'berlinspider'
    target_url = get_project_settings().get('TARGET_URL')
    start_urls = [target_url]


    def parse(self, response):
        is_exist = response.xpath("//div[@class='calendar-month-table span6']//tbody//a/@href").extract()
        if is_exist:
            print("OK")
            print(":)")
            days = response.xpath("//div[@class='calendar-month-table span6']//tbody//a/text()").extract()
            self.send_notification(days)
        else:
            print(":(")

    def send_notification(self, days):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": get_project_settings().get('PUSHOVER_TOKEN'),
            "user": get_project_settings().get('PUSHOVER_USER'),
            "message": "I found an empty slot(s)" +  ' ' + " ".join(days) + ' ' + self.target_url,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()