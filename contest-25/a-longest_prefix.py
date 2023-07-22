from collections import Counter


def solve():
    tests = int(input())
    for _ in range(tests):
        word1, word2 = input().split()
        word2 = Counter(word2)

        count = 0
        for char in word1:
            if char not in word2 or word2[char] == 0:
                break

            word2[char] -= 1
            count += 1

        print(count)

if __name__ == "__main__":
    solve()