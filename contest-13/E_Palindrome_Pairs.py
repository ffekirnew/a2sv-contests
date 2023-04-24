def solve():
    num = int(input())
    nums = []
    for _ in range(num):
        word = input()
        word_num = [0] * 26
        for char in word:
            index = ord(char) - 97
            word_num[index] ^= 1

        nums.append(int('0b' + "".join(str(num) for num in word_num)))

    print(nums)


if __name__ == "__main__":
    solve()
