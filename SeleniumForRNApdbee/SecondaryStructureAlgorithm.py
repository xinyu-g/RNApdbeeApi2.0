"""Enum containing values ​​for the 'Resolve & encode secondary structure topology using'
                        from http://rnapdbee.cs.put.poznan.pl/"""

from enum import Enum

NAME = "pseudoknotFinder"


class Algorithm(Enum):
    HYBRID ="HYBRID ALGORITHM"
    DP_ONE = "DYNAMIC PROGRAMMING"
    EG = "ELIMINATION MIN-GAIN"
    EC = "ELIMINATION MAX-CONFLICTS"
    BASIC_5P = "FIRST-COME-FIRST-SERVED"
