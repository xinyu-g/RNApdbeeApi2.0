from RNApdbee import RNApdbee3D
from RNApdbeeHtml import HtmlParser
from RNApdbeeZip import Archive

html = RNApdbee3D.execute("test_file_example\\example.pdb")

result = HtmlParser.parse3d(html)

for k, v in result[0].items():
    print(k, v)

Archive.to_archive(result, archive_format="tar")