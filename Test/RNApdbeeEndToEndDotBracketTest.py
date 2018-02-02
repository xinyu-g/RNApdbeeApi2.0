import unittest

from RNApdbeeHtml import HtmlParser
from RNApdbee import RNApdbee3D


class RNApdbeeEndToEndDotBracketTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html = RNApdbee3D.execute(pdb_id='4RDX')
        cls.result = HtmlParser.parse3d(cls.html)

    def test_dot_bracket_size(self):
        self.assertEqual(len(self.result['Dot-bracket']), 2)

    def test_dot_bracket_description(self):
        self.assertEqual(self.result['Dot-bracket'][0]['description'], ">strand_C")
        self.assertEqual(self.result['Dot-bracket'][1]['description'], ">strand_a")

    def test_dot_bracket_sequence(self):
        seq_c = "gGUGAGCGUAGCUCAGCUGGUUAGAGCACCGGACUGUGGAUCCGGGGGUCGUGGGUUCAAGUCCCAUCGCUCACCCCA"
        seq_a = "a"
        self.assertEqual(self.result['Dot-bracket'][0]['sequence'], seq_c)
        self.assertEqual(self.result['Dot-bracket'][1]['sequence'], seq_a)

    def test_dot_bracket_bracket(self):
        bracket_c = "((((((((..((((.....[...))))..(((.......-.)))......(((((..]....)))))))))))))..."
        bracket_a = "."
        self.assertEqual(self.result['Dot-bracket'][0]['bracket'], bracket_c)
        self.assertEqual(self.result['Dot-bracket'][1]['bracket'], bracket_a)