"""Html parser for Non Canonical Interactions element returned by http://rnapdbee.cs.put.poznan.pl/"""


class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and div[@class = 'column_sm1b' and " \
                "contains(text(), 'Non-canonical interactions')]]]/div[@class = 'column_sm2']//div/table/{}"

    def __init__(self, html):
        """
        :param html: object etree from lxml (wrapped html)
        """
        self.tree = html

    def get_pair(self):
        """
        :return: list of dictionaries f.e [{'Base pair': 'A.8 - A.14', 'Interaction type': 'base - base', ...}, {...}]
        """
        titles = self.tree.xpath(self.GET_VALUE.format("thead/tr/th/text()"))
        rows = self.tree.xpath(self.GET_VALUE.format("tbody/tr"))
        result = []
        for row in rows:
            values = row.xpath("./td/text()")
            result.append(dict([v for v in zip(titles, values)]))
        return result
