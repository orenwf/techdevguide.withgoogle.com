# without string
# https://techdevguide.withgoogle.com/paths/foundational/withoutstring-problem\
# -strings-base-remove-return/


def process(base, remove):
    table = {}
    for index, letter in enumerate(base):
        if letter in table:
            table[letter].append(index)
        else:
            table[letter] = [index]
    places = table[remove[0]]
    for letter in remove[1:]:
        for place in places:
            if place+1 in table[letter]:
                places.append(place+1)
    return ''.join([
        letter for index, letter in enumerate(base) if index not in places
    ])


if __name__ == 'main':
    import sys
    print(process(sys.argv[1], sys.argv[2]))
