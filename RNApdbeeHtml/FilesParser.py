"""Html parser for file (bpseq and ct) returned by http://rnapdbee.cs.put.poznan.pl/"""


class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and " \
                "div[@class = 'column_sm1b' and contains(text(), '{}')]]]/div[@class = 'column_sm2']/{}"

    BPSEQ = "BPSEQ"
    CT = "CT"

    def __init__(self, html):
        """
        :param html: object etree from lxml (wrapped html)
        """
        self.tree = html

    def get_bpseq(self):
        return self.get_file_content(self.BPSEQ)

    def get_ct(self):
        return self.get_file_content(self.CT)

    def get_file_content(self, extension):
        """
        :param extension: bpseq or ct
        :return: list of lists f.e [ [76]], [1 g 0 2 72 1], [...], ... ]
        """
        div_file = self.tree.xpath(self.GET_VALUE.format(extension, "/div/span/text()"))
        return list(map(lambda x: x.split(), div_file))
