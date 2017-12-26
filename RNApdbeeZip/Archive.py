"""This Module creates a zip or tar archive from the RNApdbeeHtml result
                in a directory where it was called. """

import os
import csv
from RNApdbeeHtml import Parser
import datetime
import shutil


def to_archive(result, archive_format='zip'):
    """
    :param result: result from RNApdbeeHtml parse2d or parse3d
    :param archive_format: zip or tar
    """
    if (archive_format != 'zip') and (archive_format != 'tar'):
        raise TypeError("Unsupported type! Use: zip or tar")

    if isinstance(result, dict):
        list_to_zip = [result]
    else:
        list_to_zip = result

    try:
        dir_result = "result_"+datetime.datetime.now().strftime("%I_%M_%p%B%d%Y")

        index = 0

        for elem in list_to_zip:

            os.makedirs("{}/result_{}".format(dir_result, index), exist_ok=True)

            if Parser.DOT_BRACKET in elem:
                content = ["\n".join(list(x.values())) for x in elem['{}'.format(Parser.DOT_BRACKET)]]
                with open("{}/result_{}/dot_bracket.txt".format(dir_result, index), "w") as outfile:
                    outfile.write("\n".join(content))

            if Parser.CT in elem:
                content = [" ".join(x) for x in elem['{}'.format(Parser.CT)]]
                with open("{}/result_{}/file.ct".format(dir_result, index), "w") as outfile:
                    outfile.write("\n".join(content))

            if Parser.BPSEQ in elem:
                content = [" ".join(x) for x in elem['{}'.format(Parser.BPSEQ)]]
                with open("{}/result_{}/file.bpseq".format(dir_result, index), "w") as outfile:
                    outfile.write("\n".join(content))

            if Parser.INTERACTIONS in elem:
                with open('{}/result_{}/interactions.csv'.format(dir_result, index), 'w', newline='') as f:
                    w = csv.DictWriter(f, elem['{}'.format(Parser.INTERACTIONS)][0].keys(), delimiter=";")
                    w.writeheader()
                    w.writerows(elem['{}'.format(Parser.INTERACTIONS)])

            if Parser.MESSAGES in elem:
                content = elem['{}'.format(Parser.MESSAGES)]
                with open("{}/result_{}/messages.txt".format(dir_result, index), "w") as outfile:
                    outfile.write("\n".join(content))

            if Parser.IMAGE in elem:
                image = elem['{}'.format(Parser.IMAGE)]
                open('{}/result_{}/image{}'.format(dir_result, index, image[1]), 'wb').write(image[0].content)

            index += 1

        shutil.make_archive("archive/{}".format(dir_result) , archive_format, dir_result)
        shutil.rmtree(dir_result)

    except IOError:
        raise Exception('Something went wrong while trying to zip result! Try again.')
