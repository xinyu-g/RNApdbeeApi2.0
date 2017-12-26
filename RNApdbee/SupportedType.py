"""This Module is used for validation of RNApdbee2D and RNApdbee3D parameters"""


def is_supported(value, type_class):
    """
    Checks if the string is in the enum class

    :param value: string
    :param type_class: enum class
    """
    supp_type = [pair.value.lower() for pair in type_class]
    if not supp_type.__contains__(value.lower()):
        raise TypeError("Unsupported type! Use: {}".format('%s' % ' or '.join(map(str, supp_type))))