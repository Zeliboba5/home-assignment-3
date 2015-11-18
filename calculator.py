from operations import operation_list


def calculate(operation, *args):
    if operation not in operation_list:
        raise ValueError("Wrong operation")

    for arg in args:
        if arg is None:
            raise ValueError("None is passed as argument")

    func = operation_list[operation]

    return func(*args)
