class Parser:

    GET_VALUE = "./fieldset/div[@class = 'main']/div/div[@class = 'column_sm2 dotbracket']"
    GET_TITLE = "./fieldset/div[@class = 'main']/div/div[@class = 'column_sm2']"

    def __init__(self, html):
        self.tree = html

    def get_structure(self):
        titles = self.tree.xpath(self.GET_TITLE)
        elements = self.tree.xpath(self.GET_VALUE)
        result = []
        for title in titles:
            text = title.xpath("./span/text()").pop(0)[1:]
            sequence = "".join(elements.pop(0).xpath("./span/text()"))
            bracket = "".join(elements.pop(0).xpath("./span/text()"))
            data = {'description': text, 'sequence': sequence, "bracket": bracket}
            result.append(data)
        return result
