def is_supported(value, type_class):
    supp_type = [pair.value.lower() for pair in type_class]
    if not supp_type.__contains__(value.lower()):
        raise TypeError("Unsupported type! Use: {}".format('%s' % ' or '.join(map(str, supp_type))))