from setuptools import setup

setup(
    name='RNApdbeeApi',
    version='1.5',
    description='Module for RNApdbee [http://rnapdbee.cs.put.poznan.pl/]',
    author='ML',
    author_email='mateusz.ligeza@student.uj.edu.pl',
    packages=['SeleniumForRNApdbee', 'RNApdbee', 'RNApdbeeHtml', 'RNApdbeeZip'],
    install_requires=['lxml', 'requests', 'selenium', ],
    package_data={'SeleniumForRNApdbee': ['driver/phantomjs_win.exe', 'driver/phantomjs_mac', 'driver/phantomjs_linux']},
)