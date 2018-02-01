"""Enum containing values ​​for the 'Generate graphical image' from http://rnapdbee.cs.put.poznan.pl/"""

from enum import Enum

NAME = "secondaryStructureDrawer"


class Graphical(Enum):
    PSEUDOVIEWER = "PSEUDO_VIEWER"
    VARNA = "VARNA"
    NONE = "NO_IMAGE"
