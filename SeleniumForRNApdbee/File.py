import os
from enum import Enum


class SupportedFile(Enum):
    PDB = ".pdb"
    BPSEQ = ".bpseq"
    CT = ".ct"


def get_supported_extension(algorithm_type):
    if algorithm_type == "3D":
        return SupportedFile.PDB.value
    elif algorithm_type == "2D":
        return "{}, {}".format(SupportedFile.BPSEQ.value, SupportedFile.CT.value)
    else:
        raise ValueError("Extension is not supported!")


def valid_file_type(absolute_path, algorithm_type):
    filename, file_extension = os.path.splitext(absolute_path)
    if algorithm_type == "3D" and file_extension.lower() == SupportedFile.PDB.value:
        return
    elif algorithm_type == "2D" and file_extension.lower() == (SupportedFile.BPSEQ.value or SupportedFile.CT.value):
        return
    else:
        raise ValueError("For {} algorithm type supported extension is {}"
                         .format(algorithm_type, get_supported_extension(algorithm_type)))