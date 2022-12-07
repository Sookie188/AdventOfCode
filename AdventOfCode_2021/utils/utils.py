def get_numbers(filename):
    with open(filename, "r") as fp:
        num = fp.readlines()
    return [int(i.rstrip()) for i in num]


def get_strings(filename):
    with open(filename, "r") as fp:
        num = fp.readlines()
    return [str(i.rstrip()) for i in num]


def split_two(list):
    result = []
    for i in range(len(list)):
        result.append(list[i].split())
    return result


def rotate_list(input):
    res = []
    for i in range(len(input[0])):
        res.append([w[i] for w in input])
    return res


def get_decimal(str):
    return int(str, 2)
