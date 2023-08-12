from math import inf


def solve():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        tastiness = list(map(int, input().split()))
        total_tastiness = sum(tastiness)

        answer = None
        p = [0]
        for i, taste in enumerate(tastiness):
            p.append(taste + p[-1])
        
        max_ = -inf
        for i in range(n - 1, -1, -1):
            if tastiness[i] >= total_tastiness:
                answer = "NO"
                break

            if i < n - 1 and p[i + 1] - 0 >= total_tastiness:
                answer = "NO"
                break

            if tastiness[i] <= 0:
                if max_ - p[i + 1] >= total_tastiness:
                    answer = "NO"
            
            max_ = max(max_, p[i + 1])

        print(answer if answer else "YES")

if __name__ == "__main__":
    solve()