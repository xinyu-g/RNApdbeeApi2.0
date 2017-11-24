from enum import Enum

NAME = "nonCanonicalHandling"


class Representation(Enum):
    TEXT_AND_GRAPHICAL = "ANALYZE_VISUALIZE"
    ONLY_GRAPHICAL = "ONLY_VISUALIZE"
    NOT_INCLUDE = "IGNORE"
