from RNApdbee import RNApdbee3D
from RNApdbeeHtml import HtmlParser
from RNApdbeeZip import Archive

html = RNApdbee3D.execute(pdb_id='4RDX')

result = HtmlParser.parse3d(html)

for k, v in result.items():
    print(k, v)

Archive.to_archive(result, archive_format="tar")