import unittest

from RNApdbeeHtml import HtmlParser
from RNApdbee import RNApdbee3D


class RNApdbeeEndToEndMessagesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html = RNApdbee3D.execute(pdb_id='4RDX')
        cls.result = HtmlParser.parse3d(cls.html)

    def test_Messages_size(self):
        self.assertEqual(len(self.result['Messages']), 23)

    def test_Messages_content(self):
        self.assertEqual(self.result['Messages'][0], 'Base-pairs identified by RNAView. ')
        self.assertEqual(self.result['Messages'][22], 'Invalid atom name in residue a.AMP501: O3P')
