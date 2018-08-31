# stringsplosion


def process(string):
    exploded_string = [string[:i+1] for i in range(0, len(string))]
    return ''.join(exploded_string)


if __name__ == 'main':
    import sys
    process(sys.argv[1])
