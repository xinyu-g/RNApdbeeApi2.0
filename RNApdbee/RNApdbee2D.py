from RNApdbee import SupportedType as Supp
from SeleniumForRNApdbee import GenerateGraphical as Gen
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as Sec
from SeleniumForRNApdbee import SeleniumDriver


def execute(file_path, secondary_structure_algorithm="hybrid", generate_graphical="pseudo_viewer"):
    Supp.is_supported(secondary_structure_algorithm, Sec.Algorithm)
    Supp.is_supported(generate_graphical, Gen.Graphical)

    selenium_driver = SeleniumDriver.Driver()
    selenium_driver.select_algorithm(Sec.Algorithm(secondary_structure_algorithm.upper()), algorithm_type="2D")
    selenium_driver.select_graphical(Gen.Graphical(generate_graphical.upper()), algorithm_type="2D")
    selenium_driver.load_file(file_path, algorithm_type="2D")
    html = selenium_driver.commit(algorithm_type="2D")
    selenium_driver.close()
    return html
