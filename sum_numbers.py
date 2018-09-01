# sum numbers


def process(string):
    return ''.join([char for char in string if not char.isdigit()])


if __name__ == 'main':
    import sys
    process(sys.argv[1])
