from collections import defaultdict


if __name__ == "__main__":
    answers = []
    number_of_test_cases = int(input())
    for test_case in range(number_of_test_cases):
        words = input().split()

        words_list = []

        for single_word in words:
            num = []
            word = []
            
            # pick the numbers from the row word
            for i, char in enumerate(single_word):
                if 47 < ord(char) < 59:
                    num.append(char)
                else:
                    word.append(char)
            num = int("".join(num))
            word = "".join(word)
            words_list.append([num, word])

        words_list.sort()
        answer = []
        for word in words_list:
            answer.append(word[1])
        answers.append(" ".join(answer))
    for answer in answers:
        print(answer)


