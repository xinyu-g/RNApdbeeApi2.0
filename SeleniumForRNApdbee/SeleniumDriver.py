"""This module controls the process for RNApdbee2D or RNApdbee3D method using selenium """

from selenium import webdriver
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as SecondaryStructure
from SeleniumForRNApdbee import GenerateGraphical as Graphical
from SeleniumForRNApdbee import BasePair
from SeleniumForRNApdbee import NonCanonical
from SeleniumForRNApdbee import FileLoader
import time
from selenium.common.exceptions import TimeoutException
from SeleniumForRNApdbee import DriverLoader
import os


class Driver:

    LINK_TO_RNAAPDBEE = 'http://rnapdbee.cs.put.poznan.pl'
    SELECT_RADIO = "//div[@id = '{}']//input[@name = '{}' and @value = '{}' and @type = 'radio']"
    SELECT_CHECKBOX = "//div[@id = 'tabs-1']//input[@name = 'analyzeHelices' and @type = 'checkbox']"
    RUN_BUTTON_ID = {"2D": "commitBpseqCt", "3D": "commitPdb"}

    def __init__(self, link=LINK_TO_RNAAPDBEE):
        phantom_js = DriverLoader.get_selenium_driver_path()
        self.driver = webdriver.PhantomJS(executable_path=phantom_js, service_log_path=os.path.devnull)
        self.driver.set_window_size(1200, 800)
        self.driver.get(link)

    def close(self):
        self.driver.close()

    @staticmethod
    def valid_type(algorithm_type):
        """

        :param algorithm_type: '3D' or '2D'
        :return: html tag for specific algorithm
        """
        if algorithm_type == "3D":
            table = "tabs-1"
        elif algorithm_type == "2D":
            table = "tabs-2"
        else:
            raise ValueError('Wrong type! Support type: 2D and 3D')
        return table

    def click_radio(self, table, name, algorithm):
        """
        chooses the radio button on the html page

        :param table: html tag for specific algorithm
        :param name: specific name for html input tag
        :param algorithm: '3D' or '2D'
        """
        self.driver.find_element_by_xpath(self.SELECT_RADIO.format(table, name, algorithm.name)).click()

    def select_algorithm_type(self, algorithm_type="3D"):
        """
        presses button for algorithm secondary structure topology on html page by name

        :param algorithm_type: '3D' or '2D'
        """
        self.driver.find_element_by_id(id_="ui-id-2" if algorithm_type == "2D" else "ui-id-1").click()

    def select_algorithm(self, algorithm, algorithm_type="3D"):
        """
        valid algorithm and presses radio button on html page for the secondary structure topology algorithm

        :param algorithm: secondary structure topology algorithm
        - HYBRID
        - DP
        - MIN_GAIN
        - MAX_CONFLICTS
        - FCFS
        :param algorithm_type: '3D' or '2D'
        """
        table = self.valid_type(algorithm_type)
        self.select_algorithm_type(algorithm_type)
        if not isinstance(algorithm, SecondaryStructure.Algorithm):
            raise ValueError('Wrong algorithm type!')
        else:
            self.click_radio(table, SecondaryStructure.NAME, algorithm)

    def select_graphical(self, graphical, algorithm_type="3D"):
        """
        valid 'graphical' and presses radio button on html page for the generate graphical image

        :param graphical: generate graphical image
        - PSEUDO_VIEWER
        - NO_IMAGE
        - VARNA
        :param algorithm_type: '3D' or '2D'
        """
        table = self.valid_type(algorithm_type)
        self.select_algorithm_type(algorithm_type)
        if not isinstance(graphical, Graphical.Graphical):
            raise ValueError('Wrong graphical type!')
        else:
            self.click_radio(table, Graphical.NAME, graphical)

    def select_identify_base_pairs(self, pair):
        """
        valid 'identify base-pairs' and presses radio button on html page for the identify base-pairs.
        only for the 3D algorithm

        :param pair: identify base-pairs.
        - RNA_VIEW
        - MC
        - DNA_DSSR
        """
        self.select_algorithm_type()
        if not isinstance(pair, BasePair.Pair):
            raise ValueError('Wrong base-pairs type!')
        else:
            self.click_radio("tabs-1", BasePair.NAME, pair)

    def select_include_non_canonical(self, non_canonical):
        """
        valid 'include non-canonical ones' and presses radio button on html page for the include non-canonical ones.
        only for the 3D algorithm

        :param non_canonical: include non-canonical ones
        - TEXT_AND_GRAPHICAL
        - ONLY_GRAPHICAL
        - NOT_INCLUDE
        """
        self.select_algorithm_type()
        if not isinstance(non_canonical, NonCanonical.Representation):
            raise ValueError('Wrong include non canonical type!')
        else:
            self.click_radio("tabs-1", NonCanonical.NAME, non_canonical)

    def insert_pdb_id(self, pdb_id):
        """
        searches tex box for pd id and put it

        :param pdb_id: pdb id from https://www.rcsb.org/
        """
        pdb_id_input = self.driver.find_element_by_id("pdbId")
        pdb_id_input.send_keys(pdb_id)

    def get_pdb_id(self):
        """
        searches button for fields pd id and presses

        """
        get = self.driver.find_element_by_xpath("//input[@value = 'Get']")
        get.click()
        
    def load_file(self, file_path, algorithm_type="3D", timeout=10):
        """
        loads the file. More info in FileLoader.py

        :param file_path:
        :param algorithm_type: '3D' or '2D'
        :param timeout:
        """
        self.valid_type(algorithm_type)
        loader = FileLoader.Loader(self.driver)
        loader.load_file(absolute_path=file_path, algorithm_type=algorithm_type, timeout=timeout)

    def commit(self, algorithm_type="3D", timeout=2):
        """
        runs the algorithm and waits for the result

        :param algorithm_type: '3D' or '2D'
        :param timeout:
        :return: the result of the algorithm in html format
        """
        self.valid_type(algorithm_type)
        run = self.driver.find_element_by_id(id_=self.RUN_BUTTON_ID.get(algorithm_type))
        self.wait_for_element(elem=run, timeout=timeout)
        run.click()
        return self.driver.page_source

    def wait_for_element(self, elem, timeout=2):
        """
        waits for a specific element on the html page.

        :param elem: disabled element
        :param timeout:
        :return:
        """
        enable = elem.is_enabled()
        if enable:
            return
        elif not enable and timeout > 0:
            time.sleep(1)
            self.wait_for_element(elem, timeout-1)
        else:
            raise TimeoutException(msg="Timeout exception when try execute!")
