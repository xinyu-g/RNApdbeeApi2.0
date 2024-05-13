"""This module is used to call the 3d function from http://rnapdbee.cs.put.poznan.pl/
    3d -> the secondary structure of RNA is derived from its tertiary structure provided in PDB file """

from RNApdbee import SupportedType as Supp
from SeleniumForRNApdbee import GenerateGraphical as Gen
from SeleniumForRNApdbee import SecondaryStructureAlgorithm as Sec
from SeleniumForRNApdbee import SeleniumDriver
from SeleniumForRNApdbee import BasePair as Bas
from SeleniumForRNApdbee import NonCanonical as Non


def execute(file_path=None, pdb_id=None, base_pairs="rna_view", non_canonical="not_include", secondary_structure_algorithm="Hybrid Algorithm"
            , generate_graphical="pseudo_viewer"):

    """
    :param file_path: path to the PDB file
    :param pdb_id: pdb id from Protein Data Bank
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

    if(file_path is None) and (pdb_id is None):
        raise ValueError('You have to specify pdb file path or pdb id from Protein Data Bank!')
    elif file_path is not None:
        selenium_driver.load_file(file_path)
        html = selenium_driver.commit()
    elif pdb_id is not None:
        selenium_driver.insert_pdb_id(pdb_id)
        selenium_driver.get_pdb_id()
        html = selenium_driver.commit(timeout=60000)

    selenium_driver.close()
    return html
    # try:
    #     Supp.is_supported(base_pairs, Bas.Pair)
    #     Supp.is_supported(non_canonical, Non.Representation)
    #     Supp.is_supported(secondary_structure_algorithm, Sec.Algorithm)
    #     Supp.is_supported(generate_graphical, Gen.Graphical)

    #     selenium_driver = SeleniumDriver.Driver()
    #     selenium_driver.select_identify_base_pairs(Bas.Pair(base_pairs.upper()))
    #     selenium_driver.select_include_non_canonical(Non.Representation(non_canonical.upper()))
    #     selenium_driver.select_algorithm(Sec.Algorithm(secondary_structure_algorithm.upper()))

    #     if(file_path is None) and (pdb_id is None):
    #         raise ValueError('You have to specify pdb file path or pdb id from Protein Data Bank!')
    #     elif file_path is not None:
    #         selenium_driver.load_file(file_path)
    #         html = selenium_driver.commit()
    #     elif pdb_id is not None:
    #         selenium_driver.insert_pdb_id(pdb_id)
    #         selenium_driver.get_pdb_id()
    #         html = selenium_driver.commit(timeout=10)

    #     selenium_driver.close()
    #     return html
    # except Exception as e:
    #     print(id, 'error:', e)
    # finally:
    #     if 'selenium_driver' in locals():
    #         selenium_driver.close()
