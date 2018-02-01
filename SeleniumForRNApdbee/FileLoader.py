"""This module loads the file for RNApdbee2D or RNApdbee3D using selenium """

import os
import time
from selenium.common.exceptions import TimeoutException
from enum import Enum


class SupportedFile(Enum):
    PDB = "pdb"
    BPSEQ = "bpseq"
    CT = "ct"


class Loader:

    SELECT_EXAMPLE_FILE = "//a[@onclick='load{}Example(1)']"
    FILE_ELEMENT_ID = {"2D": "fileBpseqCt", "3D": "filePdb"}
    CONTENT_INPUT_ID = {"Ct": "bpseqCtContentInput", "Bpseq": "bpseqCtContentInput", "Pdb": "pdbContentInput"}
    SHOW_FILE_CONTENT_ID = {"Ct": "showhideBpseqCt", "Bpseq": "showhideBpseqCt", "Pdb": "showhidePdb"}

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_supported_extension(algorithm_type):
        """
        The method returns the extension of the file for the algorithm RNApdbee2D or RNApdbee3D

        :param algorithm_type: '3D' or '2D'
        :return: pdb for 3d, ct or bpseq for 2d or throw exception
        """
        if algorithm_type == "3D":
            return SupportedFile.PDB.value
        elif algorithm_type == "2D":
            return "{} or {}".format(SupportedFile.BPSEQ.value, SupportedFile.CT.value)
        else:
            raise ValueError("Extension is not supported!")

    @staticmethod
    def get_extension(absolute_path):
        """
        Returns the file extension for the file absolut_path

        :param absolute_path: path to file
        :return: file extension
        """
        filename, file_extension = os.path.splitext(absolute_path)
        return file_extension[1:].title()

    @staticmethod
    def load_content(absolute_path):
        """
        Loads the contents of the file

        :param absolute_path: path to file
        :return: file content as text
        """
        file = open(absolute_path, 'r')
        text = file.read()
        file.close()
        return text

    def valid_type(self, absolute_path, algorithm_type):
        """
        Checks whether the file extension matches the selected algorithm.

        :param absolute_path: path to file
        :param algorithm_type: '3D' or '2D'
        :return:
        """
        file_extension = self.get_extension(absolute_path)
        if algorithm_type == "3D" and file_extension.lower() == SupportedFile.PDB.value:
            return
        elif algorithm_type == "2D" and file_extension.lower() == \
                SupportedFile.BPSEQ.value or file_extension.lower() == SupportedFile.CT.value:
            return
        else:
            raise ValueError("For {} algorithm type supported extension is {}"
                            .format(algorithm_type, self.get_supported_extension(algorithm_type)))

    def load_file(self, algorithm_type, absolute_path, timeout=10):
        """

        :param algorithm_type: '3D' or '2D'
        :param absolute_path: path to file
        :param timeout:
        """
        self.valid_type(absolute_path, algorithm_type)
        extension = self.get_extension(absolute_path)
        self.driver.find_element_by_id(id_=self.SHOW_FILE_CONTENT_ID.get(extension)).click()
        self.driver.find_element_by_xpath(self.SELECT_EXAMPLE_FILE.format(extension)).click()
        content = self.driver.find_element_by_id(id_=self.CONTENT_INPUT_ID.get(extension))
        self.clear_content(content, timeout)
        self.set_content(absolute_path)
        self.driver.find_element_by_id(id_=self.SHOW_FILE_CONTENT_ID.get(extension)).click()

    def set_content(self, absolute_path):
        """
        Inserts the contents of the file on the page http://rnapdbee.cs.put.poznan.pl/

        :param absolute_path: path to file
        """
        file_content = self.load_content(absolute_path)
        extension = self.get_extension(absolute_path)
        content = self.driver.find_element_by_id(id_=self.CONTENT_INPUT_ID.get(extension))
        self.driver.execute_script("arguments[0].value = arguments[1];", content, file_content)

    def clear_content(self, elem, timeout=10):
        """
        Clear the contents of the file on the page http://rnapdbee.cs.put.poznan.pl/

        :param elem: text box contains seq
        :param timeout:
        :return:
        """
        value = elem.get_attribute("value")
        if len(value) > 0:
            return
        elif timeout > 0:
            time.sleep(1)
            self.clear_content(elem, timeout-1)
        else:
            raise TimeoutException(msg="Something went wrong")

