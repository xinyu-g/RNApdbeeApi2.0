import requests


class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and " \
                "div[@class = 'column_sm1b' and contains(text(), '{}')]]]/div[@class = 'column_sm2']/{}"

    def __init__(self, html):
        self.tree = html

    def get_image(self):
        href = self.tree.xpath(self.GET_VALUE.format("Image", "/a/@href"))
        response = requests.get("http://rnapdbee.cs.put.poznan.pl{}".format(href[0]), allow_redirects=True)
        return response

