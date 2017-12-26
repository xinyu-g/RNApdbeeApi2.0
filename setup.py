from setuptools import setup

setup(
    name='RNApdbeeApi',
    version='1.4',
    description='Module for RNApdbee [http://rnapdbee.cs.put.poznan.pl/]',
    author='ML',
    author_email='mateusz.ligeza@student.uj.edu.pl',
    packages=['SeleniumForRNApdbee', 'RNApdbee', 'RNApdbeeHtml', 'RNApdbeeZip'],
    install_requires=['lxml', 'requests', 'selenium', ],
    package_data={'SeleniumForRNApdbee': ['driver/phantomjs.exe']},
)