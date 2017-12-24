from lxml import etree
from RNApdbeeHtml import Parser


def parse2d(html, dot_bracket=True, ct=True, bpseq=True, image=True, size=10):
    tree = etree.HTML(html)
    parts = tree.xpath("//form[@id = 'downloadResults']")
    final_list = []
    for part in parts:
        if size == 0:
            break
        size -= 1
        result = {}
        if dot_bracket is True:
            result['{}'.format(Parser.DOT_BRACKET)] = Parser.get_dot_bracket(part)
        if bpseq is True:
            result['{}'.format(Parser.BPSEQ)] = Parser.get_bpseq(part)
        if ct is True:
            result['{}'.format(Parser.CT)] = Parser.get_ct(part)
        if image is True:
            result['{}'.format(Parser.IMAGE)] = Parser
        final_list.append(result)
    if len(final_list) == 1:
        return final_list[0]
    else:
        return final_list


def parse3d(html, dot_bracket=True, ct=True, bpseq=True, image=True, non_canonical=True, messages=True, size=10):
    tree = etree.HTML(html)
    parts = tree.xpath("//form[@id = 'downloadResults']")
    final_list = []
    for part in parts:
        if size == 0:
            break
        size -= 1
        result = {}
        if dot_bracket is True:
            result['{}'.format(Parser.DOT_BRACKET)] = Parser.get_dot_bracket(part)
        if bpseq is True:
            result['{}'.format(Parser.BPSEQ)] = Parser.get_bpseq(part)
        if ct is True:
            result['{}'.format(Parser.CT)] = Parser.get_ct(part)
        if messages is True:
            result['{}'.format(Parser.MESSAGES)] = Parser.get_messages(part)
        if non_canonical is True:
            result['{}'.format(Parser.INTERACTIONS)] = Parser.get_interactions(part)
        if image is True:
            result['{}'.format(Parser.IMAGE)] = Parser.get_image(part)
        final_list.append(result)
    if len(final_list) == 1:
        return final_list[0]
    else:
        return final_list
