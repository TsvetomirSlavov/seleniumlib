

def exec_only_if_integer_parameter(f):
    def validate_index(self, index):
        if not isinstance(index, int):
            return
        f(self, index)
    return validate_index


def exec_only_if_not_none_parameter(f):
    def validate_index(self, parameter):
        if parameter is None:
            return
        f(self, parameter)
    return validate_index
