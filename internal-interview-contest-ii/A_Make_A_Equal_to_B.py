from collections import Counter

def count_disparity(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

    return count

def count_and(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i] == '1':
            count += 1

    return count

def bit_counter(a):
    freq = Counter(a)
    if '1' not in freq:
        freq['1'] = 0
    
    return freq['1']


class MakeAEqualToB:
    def solve(self):
        tests = int(input())
        for _ in range(tests):
            n = int(input())
            a = input().split()
            b = input().split()

            # print(a, '-', sorted(a))
            # print(a, b, count_disparity(a, b), count_disparity(sorted(a), sorted(b)))

            if count_disparity(a, b) == 0:
                print(0)
            elif count_disparity(sorted(a), sorted(b)) == 0:
                print(1)
            else:
                and_count = count_and(a, b)
                a_count = bit_counter(a) - and_count
                b_count = bit_counter(b) - and_count

                if not a_count or not b_count:
                    print(max(a_count, b_count))
                else:
                    print(1 + abs(a_count - b_count))


if __name__ == "__main__":
    solution = MakeAEqualToB()
    solution.solve()
