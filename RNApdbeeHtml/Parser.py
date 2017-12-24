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
    file_parts = FilesParser.Parser(part)
    return file_parts.get_bpseq()


def get_ct(part):
    file_parts = FilesParser.Parser(part)
    return file_parts.get_ct()


def get_dot_bracket(part):
    dot_parser = DotBracketParser.Parser(part)
    return dot_parser.get_structure()


def get_image(part):
    image = ImageParser.Parser(part)
    return image.get_image()


def get_messages(part):
    message_parser = MessagesParser.Parser(part)
    return message_parser.get_messages()


def get_interactions(part):
    non = NonCanonicalInteractionsParser.Parser(part)
    return non.get_pair()