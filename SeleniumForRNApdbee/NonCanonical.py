from enum import Enum

NAME = "nonCanonicalHandling"


class Representation(Enum):
    ANALYZE_VISUALIZE = "TEXT_AND_GRAPHICAL"
    ONLY_VISUALIZE = "ONLY_GRAPHICAL"
    IGNORE = "NOT_INCLUDE"
