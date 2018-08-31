# longest common subsequence


def lcs(string, *words):
    freq = {}
    for index, letter in enumerate(string):
        if letter in freq:
            freq[letter].append(index)
        else:
            freq[letter] = [index]
    print(freq)
    longest = '', 0
    for word in words:
        current = 0
        for index, letter in enumerate(word):
            if letter in freq:
                if index+current in freq[letter]:
                    current += 1
                    if current > longest[1]:
                        longest = word, current
        print(longest)


if __name__ == 'main':
    import sys
    lcs(sys.argv[1], sys.argv[1:])
