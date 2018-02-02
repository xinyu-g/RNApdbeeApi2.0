import unittest

from RNApdbee import SupportedType
from SeleniumForRNApdbee import GenerateGraphical as Gen
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as Sec
from SeleniumForRNApdbee import BasePair as Bas
from SeleniumForRNApdbee import NonCanonical as Non


class RNApdbeeTest(unittest.TestCase):

    def test_graphical(self):
        self.assertRaises(TypeError, lambda: SupportedType.is_supported("not supported type", Gen.Graphical))

    def test_basePair(self):
        self.assertRaises(TypeError, lambda: SupportedType.is_supported("not supported type", Bas.Pair))

    def test_non_canonical(self):
        self.assertRaises(TypeError, lambda: SupportedType.is_supported("not supported type", Non.Representation))

    def test_secondary_structure_algorithm(self):
        self.assertRaises(TypeError, lambda: SupportedType.is_supported("not supported type", Sec.Algorithm))
