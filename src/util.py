def generate_snail_positions(array_size):
    x = 0
    y = 0
    limit = {"top": 0, "bottom": array_size - 1, "right": array_size - 1, "left": 0}

    for _ in range(array_size // 2 + 1):

        while x < limit["right"]:
            yield (x, y)
            x += 1
        limit["top"] += 1

        while y < limit["bottom"]:
            yield (x, y)
            y += 1
        limit["right"] -= 1

        while x > limit["left"]:
            yield (x, y)
            x -= 1
        limit["bottom"] -= 1

        while y > limit["top"]:
            yield (x, y)
            y -= 1
        limit["left"] += 1
    yield (x, y)


def flatten_nested_list(nested_list):
    return [item for elem in nested_list for item in elem]


class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
