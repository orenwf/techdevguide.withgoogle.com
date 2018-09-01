# can balance


def process(list):
    i = 0
    j = -1
    i_sum = list[i]
    j_sum = list[j]
    while i - j + 1 < len(list):
        if i_sum <= j_sum:
            i += 1
            i_sum += list[i]
        else:
            j -= 1
            j_sum += list[j]
    return i_sum == j_sum


if __name__ == 'main':
    import sys.argv
    process(sys.argv[1])
