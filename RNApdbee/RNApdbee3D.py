"""This module is used to call the 3d function from http://rnapdbee.cs.put.poznan.pl/
    3d -> the secondary structure of RNA is derived from its tertiary structure provided in PDB file """

from RNApdbee import SupportedType as Supp
from SeleniumForRNApdbee import GenerateGraphical as Gen
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as Sec
from SeleniumForRNApdbee import SeleniumDriver
from SeleniumForRNApdbee import BasePair as Bas
from SeleniumForRNApdbee import NonCanonical as Non


def execute(file_path, base_pairs="rna_view", non_canonical="not_include", secondary_structure_algorithm="hybrid"
            , generate_graphical="pseudo_viewer"):

    """
    :param file_path: path to the PDB file
    :param base_pairs: possible values: [rna_view, mc, dna_dssr]
    :param non_canonical: possible values: [text_and_graphical, only_graphical, not_include]
    :param secondary_structure_algorithm: possible values: [hybrid, dp, min_gain, max_conflicts, fcfs]
    :param generate_graphical: possible values: [pseudo_viewer, varna, no_image]
    :return: html with result from http://rnapdbee.cs.put.poznan.pl/ for 3d
    """
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
