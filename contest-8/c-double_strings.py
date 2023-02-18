tests = int(input())
answers = []

for _ in range(tests):

    n = int(input())
    strings = [ input() for _ in range(n) ]
    string_set = set( strings )

    answers.append([])

    for string in strings:
        added = False

        for i in range( len(string) ):

            part1 = string[:i]

            if part1 in string_set:
                if string[i:] in string_set:
                    answers[-1].append('1')
                    added = True

                    break

        if not added:
            answers[-1].append('0')


for answer in answers:
    print("".join(answer))


