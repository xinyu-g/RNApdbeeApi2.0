from RNApdbee import SupportedType as Supp
from SeleniumForRNApdbee import GenerateGraphical as Gen
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as Sec
from SeleniumForRNApdbee import SeleniumDriver
from SeleniumForRNApdbee import BasePair as Bas
from SeleniumForRNApdbee import NonCanonical as Non


def execute(file_path, base_pairs="rna_view", non_canonical="not_include", secondary_structure_algorithm="hybrid"
            , generate_graphical="pseudo_viewer"):

    Supp.is_supported(base_pairs, Bas.Pair)
    Supp.is_supported(non_canonical, Non.Representation)
    Supp.is_supported(secondary_structure_algorithm, Sec.Algorithm)
    Supp.is_supported(generate_graphical, Gen.Graphical)

    selenium_driver = SeleniumDriver.Driver()
    selenium_driver.select_identify_base_pairs(Bas.Pair(base_pairs.upper()))
    selenium_driver.select_include_non_canonical(Non.Representation(non_canonical.upper()))
    selenium_driver.select_algorithm(Sec.Algorithm(secondary_structure_algorithm.upper()))
    selenium_driver.load_file(file_path)
    html = selenium_driver.commit()
    selenium_driver.close()
    return html
