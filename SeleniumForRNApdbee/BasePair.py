"""Enum containing values ​​for the 'Identify base-pairs' from http://rnapdbee.cs.put.poznan.pl/"""

from enum import Enum

NAME = "basePairAnalyzer"


class Pair(Enum):
    RNAVIEW = "RNA_VIEW"
    MCANNOTATE = "MC"
    DSSR = "DNA_DSSR"
