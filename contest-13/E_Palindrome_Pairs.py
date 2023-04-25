from collections import defaultdict


def accept_word_input(num):
    words = []
    for _ in range(num):
        alphabet = ['0'] * 26
        word = input()
        for char in word:
            if alphabet[ord(char) - 97] == '0':
                alphabet[ord(char) - 97] = '1'
            else:
                alphabet[ord(char) - 97] = '0'

        variations = [alphabet]
        for i in range(len(alphabet)):
            if alphabet[i] == '1':
                alphabet[i] = '0'
                variations.append(alphabet.copy())
                alphabet[i] = '1'
        words.append([int("0b" + "".join(alphabet), 2) for alphabet in variations])

    words.sort()

    return words


def solve():
    num = int(input())
    words = accept_word_input(num)
    answer = 0
    freq = defaultdict(int)

    print(words)

    for variation in words:
        for variant in variation:
            if variant in freq:
                answer += freq[variant]

            freq[variation[0]] += 1

    print(answer)


if __name__ == "__main__":
    solve()
