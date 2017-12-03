import os
import time
from selenium.common.exceptions import TimeoutException
from enum import Enum


class SupportedFile(Enum):
    PDB = ".pdb"
    BPSEQ = ".bpseq"
    CT = ".ct"


class Loader:

    SELECT_EXAMPLE_FILE = "//a[@onclick='load{}Example(1)']"
    FILE_ELEMENT_ID = {"2D": "fileBpseqCt", "3D": "filePdb"}
    CONTENT_INPUT_ID = {"Ct": "bpseqCtContentInput", "Bpseq": "bpseqCtContentInput", "Pdb": "pdbContentInput"}
    SHOW_FILE_CONTENT_ID = {"Ct": "showhideBpseqCt", "Bpseq": "showhideBpseqCt", "Pdb": "showhidePdb"}

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_supported_extension(algorithm_type):
        if algorithm_type == "3D":
            return SupportedFile.PDB.value
        elif algorithm_type == "2D":
            return "{} or {}".format(SupportedFile.BPSEQ.value, SupportedFile.CT.value)
        else:
            raise ValueError("Extension is not supported!")

    @staticmethod
    def get_extension(absolute_path):
        filename, file_extension = os.path.splitext(absolute_path)
        return file_extension[1:].title()

    @staticmethod
    def load_content(absolute_path):
        file = open(absolute_path, 'r')
        text = file.read()
        file.close()
        return text

    def valid_type(self, absolute_path, algorithm_type):
        filename, file_extension = os.path.splitext(absolute_path)
        if algorithm_type == "3D" and file_extension.lower() == SupportedFile.PDB.value:
            return
        elif algorithm_type == "2D" and file_extension.lower() == \
                SupportedFile.BPSEQ.value or file_extension.lower() == SupportedFile.CT.value:
            return
        else:
            raise ValueError("For {} algorithm type supported extension is {}"
                            .format(algorithm_type, self.get_supported_extension(algorithm_type)))

    def load_file(self, algorithm_type, absolute_path, timeout=2):
        self.valid_type(absolute_path, algorithm_type)
        extension = self.get_extension(absolute_path)
        self.driver.find_element_by_xpath(self.SELECT_EXAMPLE_FILE.format(extension)).click()
        self.driver.find_element_by_id(id_=self.SHOW_FILE_CONTENT_ID.get(extension)).click()
        self.clear_content(absolute_path, timeout)
        self.set_content(absolute_path)
        self.driver.find_element_by_id(id_=self.SHOW_FILE_CONTENT_ID.get(extension)).click()

    def clear_content(self, absolute_path, timeout=2):
        extension = self.get_extension(absolute_path)
        content = self.driver.find_element_by_id(id_=self.CONTENT_INPUT_ID.get(extension))
        self.wait_for_file_load(content, timeout)
        content.clear()

    def set_content(self, absolute_path):
        file_content = self.load_content(absolute_path)
        extension = self.get_extension(absolute_path)
        content = self.driver.find_element_by_id(id_=self.CONTENT_INPUT_ID.get(extension))
        content.send_keys(file_content)

    def wait_for_file_load(self, elem, timeout=2):
        displayed = elem.is_displayed()
        if displayed:
            return
        elif not displayed and timeout > 0:
            time.sleep(1)
            self.wait_for_file_load(elem, timeout-1)
        else:
            raise TimeoutException(msg="Timeout exception when loading a file")

