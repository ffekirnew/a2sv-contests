if __name__ == "__main__":
    answers = []
    number_of_test_cases = int(input())
    for test_case in range(number_of_test_cases):
        word = input()
        idx = 0
        answer = []
        for idx in range(2):
            answer.append(word[idx])
        for char in "... ":
            answer.append(char)
        for idx in range(len(word)):
            answer.append(word[idx])
        answer.append("?")
        answers.append("".join(answer))
    for answer in answers:
        print(answer)
