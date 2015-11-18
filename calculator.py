from operations import operation_list


def calculate(operation, *args):
    if operation not in operation_list:
        raise ValueError("Wrong operation")

    for arg in args:
        if not isinstance(arg, basestring):
            raise ValueError("Pass string as argument please")

    func = operation_list[operation]

    return func(*args)
