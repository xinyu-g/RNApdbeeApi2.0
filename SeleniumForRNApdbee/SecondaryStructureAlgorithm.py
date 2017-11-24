from enum import Enum

NAME = "pseudoknotFinder"


class Algorithm(Enum):
    HYBRID = "COMPLEX_HYBRID"
    DP = "DP_ONE"
    MIN_GAIN = "EG"
    MAX_CONFLICTS = "EC"
    FCFS = "BASIC_5P"
