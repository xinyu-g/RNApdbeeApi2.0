class Parser:

    GET_VALUE = "./fieldset/div[div[@class = 'column_sm1' and " \
                "div[@class = 'column_sm1b' and contains(text(), '{}')]]]/div[@class = 'column_sm2']/{}"

    def __init__(self, html):
        self.tree = html

    def get_pair(self):
        column_name = self.tree.xpath(self.GET_VALUE.format("Non-canonical interactions", "/div/table/thead/tr/th/text()"))
        print(column_name)