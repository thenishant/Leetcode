from collections import Counter


def closeStrings(word1, word2):
    c1, c2 = Counter(word1), Counter(word2)
    return sorted(c1.values()) == sorted(c2.values()) and sorted(c1.keys()) == sorted(c2.keys())


if __name__ == '__main__':
    print(closeStrings('abbccc', 'abbbcc'))
    print(closeStrings('uau', 'ssx'))
