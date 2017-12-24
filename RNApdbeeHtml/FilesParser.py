class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and " \
                "div[@class = 'column_sm1b' and contains(text(), '{}')]]]/div[@class = 'column_sm2']/{}"

    BPSEQ = "BPSEQ"
    CT = "CT"

    def __init__(self, html):
        self.tree = html

    def get_bpseq(self):
        return self.get_file_content(self.BPSEQ)

    def get_ct(self):
        return self.get_file_content(self.CT)

    def get_file_content(self, extension):
        div_file = self.tree.xpath(self.GET_VALUE.format(extension, "/div/span/text()"))
        return list(map(lambda x: x.split(), div_file))
