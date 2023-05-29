from math import inf


def solve():
    tests = int(input())
    for _ in range(tests):
        number= list(input())

        next = {'5': ['2', '7'], '0': ['0', 5]}
        seen = {}

        answer = inf

        for i in range(len(number) - 1, -1, -1):
            if '5' not in seen and '0' not in seen:
                pass
            else:
                if '5' in seen:
                    if number[i] in seen:
                        pass
                    if '7' in seen:
                        pass

                if '0' in seen:
                    pass
        

if __name__ == "__main__":
    solve()