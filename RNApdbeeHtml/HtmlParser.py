"""This Module parses html returned from RNApdbee2D or RNApdbee3D"""

from lxml import etree
from RNApdbeeHtml import Parser


def parse2d(html, dot_bracket=True, ct=True, bpseq=True, image=True, size=10):
    """
    parses html from RNApdbee2D

    :param html: html returned from http://rnapdbee.cs.put.poznan.pl after execution
    :param dot_bracket: if true then result include dot brackets
    :param ct: if true then result include ct file
    :param bpseq: if true then result include bpseq file
    :param image: if true then result include image
    :param size: result list max size
    :return: list of dictionaries or one dictionaries f.e

    {
        Dot-bracket: [{'description': '>strand_A', 'sequence': 'gGGACCUUCCCGGUCUC', 'bracket': '.(((((.....))))).'}],
        CT [['17'], ['1', 'g', '0', '2', '0', '1'], ['2', 'G', '1', '3', '16', '2'], ['3', 'G', '2', '4'], ...],
        BPSEQ [['1', 'g', '0'], ['2', 'G', '16'], ['3', 'G', '15'], ['4', 'A', '14'], ['5', 'C', '13'], ...],
        Image [<Response [200]>, '.svg']
    }
    """
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
            result['{}'.format(Parser.IMAGE)] = Parser.get_image(part)
        final_list.append(result)
    if len(final_list) == 1:
        return final_list[0]
    else:
        return final_list


def parse3d(html, dot_bracket=True, ct=True, bpseq=True, image=True, non_canonical=True, messages=True, size=10):
    """
    parses html from RNApdbee3D

    :param html: html returned from http://rnapdbee.cs.put.poznan.pl after execution
    :param dot_bracket: if true then result include dot brackets
    :param ct: if true then result include ct file
    :param bpseq: if true then result include bpseq file
    :param image: if true then result include image
    :param non_canonical: if true then result include non canonical interactions
    :param messages: if true then result include messages
    :param size: result list max size
    :return: list of dictionaries or one dictionaries f.e

    {
        Dot-bracket: [{'description': '>strand_A', 'sequence': 'gGGACCUUCCCGGUCUC', 'bracket': '.(((((.....))))).'}],
        CT [['17'], ['1', 'g', '0', '2', '0', '1'], ['2', 'G', '1', '3', '16', '2'], ['3', 'G', '2', '4'], ...],
        BPSEQ [['1', 'g', '0'], ['2', 'G', '16'], ['3', 'G', '15'], ['4', 'A', '14'], ['5', 'C', '13'], ...],
        Image [<Response [200]>, '.svg'],
        Non-canonical-interactions [{'Base pair': 'A.1 - A.17', 'Interaction type': 'base - base', ...}, {...}, {...} ],
        Messages ['Base-pairs identified by RNAView. ', 'Graphical image generated by PseudoViewer-based procedure']
    }
    """
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
