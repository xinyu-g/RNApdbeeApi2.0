"""This module calls specific parsers."""

from RNApdbeeHtml import FilesParser
from RNApdbeeHtml import MessagesParser
from RNApdbeeHtml import DotBracketParser
from RNApdbeeHtml import NonCanonicalInteractionsParser
from RNApdbeeHtml import ImageParser

BPSEQ = "BPSEQ"
CT = "CT"
DOT_BRACKET = 'Dot-bracket'
IMAGE = 'Image'
MESSAGES = 'Messages'
INTERACTIONS = 'Non-canonical-interactions'


def get_bpseq(part):
    """
    calls FilesParser for bpseq file

    :param part: object etree from lxml (wrapped html)
    :return: list of lists f.e [ [76]], [1 g 0 2 72 1], [...], ... ]
    """
    file_parts = FilesParser.Parser(part)
    return file_parts.get_bpseq()


def get_ct(part):
    """
    calls FilesParser for ct file

    :param part: object etree from lxml (wrapped html)
    :return: list of lists f.e [ [76]], [1 g 0 2 72 1], [...], ... ]
    """
    file_parts = FilesParser.Parser(part)
    return file_parts.get_ct()


def get_dot_bracket(part):
    """
    calls DotBracketParser

    :param part: object etree from lxml (wrapped html)
    :return: list of dictionaries f.e [{'description': 'strand_A', 'sequence': 'gCGG', "bracket": '(((((', {...}]
    """
    dot_parser = DotBracketParser.Parser(part)
    return dot_parser.get_structure()


def get_image(part):
    """
    calls ImageParser

    :param part: object etree from lxml (wrapped html)
    :return: list with requests object contains image and image extension
    """
    image = ImageParser.Parser(part)
    return image.get_image()


def get_messages(part):
    """
    calls MessagesParser

    :param part: object etree from lxml (wrapped html)
    :return: list with messages f.e ['example1', 'example2', ...]
    """
    message_parser = MessagesParser.Parser(part)
    return message_parser.get_messages()


def get_interactions(part):
    """
    calls NonCanonicalInteractionsParser

    :param part: object etree from lxml (wrapped html)
    :return: list of dictionaries f.e [{'Base pair': 'A.8 - A.14', 'Interaction type': 'base - base', ...}, {...}]
    """
    non = NonCanonicalInteractionsParser.Parser(part)
    return non.get_pair()