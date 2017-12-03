from selenium import webdriver
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as SecondaryStructure
from SeleniumForRNApdbee import GenerateGraphical as Graphical
from SeleniumForRNApdbee import BasePair
from SeleniumForRNApdbee import NonCanonical
from SeleniumForRNApdbee import FileLoader


class Driver:

    LINK_TO_RNAAPDBEE = 'http://rnapdbee.cs.put.poznan.pl'
    SELECT_RADIO = "//div[@id = '{}']//input[@name = '{}' and @value = '{}' and @type = 'radio']"
    SELECT_CHECKBOX = "//div[@id = 'tabs-1']//input[@name = 'analyzeHelices' and @type = 'checkbox']"
    RUN_BUTTON_ID = {"2D": "commitBpseqCt", "3D": "commitPdb"}

    def __init__(self, link=LINK_TO_RNAAPDBEE):
        self.driver = webdriver.PhantomJS("C:\\Users\\zaloguj\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
        self.driver.set_window_size(1200, 800)
        self.driver.get(link)

    def close(self):
        self.driver.close()

    def click_radio(self, table, name, algorithm):
        self.driver.find_element_by_xpath(self.SELECT_RADIO.format(table, name, algorithm.name)).click()

    @staticmethod
    def valid_type(algorithm_type):
        if algorithm_type == "3D":
            table = "tabs-1"
        elif algorithm_type == "2D":
            table = "tabs-2"
        else:
            raise ValueError('Wrong type! Support type: 2D and 3D')
        return table

    def select_algorithm_type(self, algorithm_type="3D"):
        self.driver.find_element_by_id(id_="ui-id-2" if algorithm_type == "2D" else "ui-id-1").click()

    def select_algorithm(self, algorithm, algorithm_type="3D"):
        table = self.valid_type(algorithm_type)
        self.select_algorithm_type(algorithm_type)
        if not isinstance(algorithm, SecondaryStructure.Algorithm):
            raise ValueError('Wrong algorithm type!')
        else:
            self.click_radio(table, SecondaryStructure.NAME, algorithm)

    def select_graphical(self, graphical, algorithm_type="3D"):
        table = self.valid_type(algorithm_type)
        self.select_algorithm_type(algorithm_type)
        if not isinstance(graphical, Graphical.Graphical):
            raise ValueError('Wrong graphical type!')
        else:
            self.click_radio(table, Graphical.NAME, graphical)

    def select_identify_base_pairs(self, pair):
        self.select_algorithm_type()
        if not isinstance(pair, BasePair.Pair):
            raise ValueError('Wrong base-pairs type!')
        else:
            self.click_radio("tabs-1", BasePair.NAME, pair)

    def select_include_non_canonical(self, non_canonical):
        self.select_algorithm_type()
        if not isinstance(non_canonical, NonCanonical.Representation):
            raise ValueError('Wrong include non canonical type!')
        else:
            self.click_radio("tabs-1", NonCanonical.NAME, non_canonical)

    def select_analyse_helices(self):
        self.driver.find_element_by_xpath(self.SELECT_CHECKBOX).click()
        
    def load_file(self, file_path, algorithm_type="3D", timeout=2):
        self.valid_type(algorithm_type)
        loader = FileLoader.Loader(self.driver)
        loader.load_file(absolute_path=file_path, algorithm_type=algorithm_type, timeout=timeout)

    def commit(self, algorithm_type="3D"):
        self.valid_type(algorithm_type)
        self.driver.find_element_by_id(id_=self.RUN_BUTTON_ID.get(algorithm_type)).click()
        return self.driver.page_source
