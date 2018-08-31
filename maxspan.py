# maxspan


def process(sequence):
    table = {}
    for i, v in enumerate(sequence):
        if v in table:
            table[v].append(i)
        else:
            table[v] = [i]
    max_span = None,0
    for k, v in table.items():
        current_span = v[-1]-v[0]+1
        if current_span > max_span[1]:
            max_span = k, current_span
    return max_span


if __name__ == 'main':
    import sys
    process(sys.argv[1])
