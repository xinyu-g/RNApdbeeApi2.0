"""Html parser for Messages element returned by http://rnapdbee.cs.put.poznan.pl/"""


class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and " \
                "div[@class = 'column_sm1b' and contains(text(), '{}')]]]/div[@class = 'column_sm2']/{}"

    def __init__(self, html):
        """
        :param html: object etree from lxml (wrapped html)
        """
        self.tree = html

    def get_messages(self):
        """
        :return: list with messages f.e ['example1', 'example2', ...]
        """
        return self.tree.xpath(self.GET_VALUE.format("Messages", "/div/ol/li/text()"))
