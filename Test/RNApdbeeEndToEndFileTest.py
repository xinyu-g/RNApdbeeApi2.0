import unittest

from RNApdbeeHtml import HtmlParser
from RNApdbee import RNApdbee3D


class RNApdbeeEndToEndFileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html = RNApdbee3D.execute(pdb_id='4RDX')
        cls.result = HtmlParser.parse3d(cls.html)

    def test_BPSEQ_size(self):
        self.assertEqual(len(self.result['BPSEQ']), 79)

    def test_BPSEQ_content(self):
        self.assertEqual(self.result['BPSEQ'][0], ['1', 'g', '75'])
        self.assertEqual(self.result['BPSEQ'][78], ['79', 'a', '0'])

    def test_CT_size(self):
        self.assertEqual(len(self.result['CT']), 80)

    def test_CT_content(self):
        self.assertEqual(self.result['CT'][0], ['79'])
        self.assertEqual(self.result['CT'][1], ['1', 'g', '0', '2', '75', '-1'])
        self.assertEqual(self.result['CT'][79], ['79', 'a', '0', '0', '0', '501'])
