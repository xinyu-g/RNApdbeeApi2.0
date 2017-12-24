class Parser:

    GET_VALUE = "./fieldset/div[@class = 'main']/div/div[@class = 'column_sm2' or @class = 'column_sm2 dotbracket']"

    def __init__(self, html):
        self.tree = html

    def get_structure(self):
        elements = self.tree.xpath(self.GET_VALUE)
        result = []
        for elem in elements:
            text = elem.xpath("./span/text()")
            if any(" " in s for s in text):
                result.append("".join(text)[1:])
            else:
                result.append("".join(text))
        return "\n".join(result)
