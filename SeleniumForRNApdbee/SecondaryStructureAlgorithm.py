from enum import Enum

NAME = "pseudoknotFinder"


class Algorithm(Enum):
    COMPLEX_HYBRID ="HYBRID"
    DP_ONE = "DP"
    EG = "MIN_GAIN"
    EC = "MAX_CONFLICTS"
    BASIC_5P = "FCFS"
