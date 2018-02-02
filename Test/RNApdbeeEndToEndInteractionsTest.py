import unittest

from RNApdbeeHtml import HtmlParser
from RNApdbee import RNApdbee3D


class RNApdbeeEndToEndInteractionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html = RNApdbee3D.execute(pdb_id='4RDX')
        cls.result = HtmlParser.parse3d(cls.html)

    def test_Interaction_size(self):
        self.assertEqual(len(self.result['Non-canonical-interactions']), 21)

    def test_Interaction_content(self):
        self.assertEqual(self.result['Non-canonical-interactions'][0]['Base pair'], 'C.8 - C.14')
        self.assertEqual(self.result['Non-canonical-interactions'][0]['Interaction type'], 'base - base')
        self.assertEqual(self.result['Non-canonical-interactions'][20]['Base pair'], 'C.60 - C.61')
        self.assertEqual(self.result['Non-canonical-interactions'][20]['Interaction type'], 'other')

