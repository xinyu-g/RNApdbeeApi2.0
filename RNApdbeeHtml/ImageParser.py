"""Html parser for image returned by http://rnapdbee.cs.put.poznan.pl/"""

import requests
import os


class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and " \
                "div[@class = 'column_sm1b' and contains(text(), '{}')]]]/div[@class = 'column_sm2']/{}"

    def __init__(self, html):
        """
        :param html: object etree from lxml (wrapped html)
        """
        self.tree = html

    def get_image(self):
        """
        :return: list with requests object contains image and image extension
        """
        href = self.tree.xpath(self.GET_VALUE.format("Image", "/a/@href"))
        filename, file_extension = os.path.splitext(href[0])
        response = requests.get("http://rnapdbee.cs.put.poznan.pl{}".format(href[0]), allow_redirects=True)
        return [response, file_extension]

