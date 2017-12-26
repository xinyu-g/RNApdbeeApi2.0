from RNApdbee import RNApdbee3D
from RNApdbeeHtml import HtmlParser
from RNApdbeeZip import Archive

html = RNApdbee3D.execute("driver\\example.pdb")

result = HtmlParser.parse3d(html)

Archive.to_archive(result, archive_format="tar")