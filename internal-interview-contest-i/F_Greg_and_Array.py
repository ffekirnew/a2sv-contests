def solve():
    n, m, k = list(map(int, input().split()))
    array = list(map(int, input().split()))

    operations = [list(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(k)]

    process_queries = [0] * (n + 1)
    for left, right, value in operations:
        process_queries[right] += value
        process_queries[left -1] -= value

    prefix_sum = [0]
    for number in process_queries:
        prefix_sum.append(prefix_sum[-1] + number)
    
    print(prefix_sum)

if __name__ == "__main__":
    solve()
