num_tests = int(input())
answers = []

for test in range(num_tests):
    string = input()
    answers.append([])

    if len(string) == 1 or string[0] != string[1]:
        answers[-1].append(string[0])

    for i in range(1, len(string) - 1):
        if string[i - 1] != string[i] and string[i] != string[i + 1]:
            answers[-1].append(string[i])

    if len(string) > 1 and string[-1] != string[-2]:
        answers[-1].append(string[-1])

    answers[-1].sort()

for answer in answers:
    print("".join(answer))