if __name__ == "__main__":
    tests = int(input())
    results = []

    for test in range(tests):
        results.append([])

        n, m, k = map( int, input().split() )
        string_n = list( input() )
        string_m = list( input() )

        string_n.sort()
        string_m.sort()

        op_counter_1, op_counter_2 = 0, 0

        p1, p2 = 0, 0

        while p1 < n and p2 < m:
            if string_n[p1] < string_m[p2]:
                if op_counter_1 < k:
                    results[-1].append(string_n[p1])
                    op_counter_1 += 1
                    op_counter_2 = 0
                    p1 += 1
                elif op_counter_2 < k:
                    results[-1].append(string_m[p2])
                    p2 += 1
                    op_counter_2 += 1
                    op_counter_1 = 0
            else:
                if op_counter_2 < k:
                    results[-1].append(string_m[p2])
                    p2 += 1
                    op_counter_2 += 1
                    op_counter_1 = 0
                elif op_counter_1 < k:
                    results[-1].append(string_n[p1])
                    op_counter_1 += 1
                    op_counter_2 = 0
                    p1 += 1
    for result in results:
        print("".join(result))
                


        