class Copies:
    def solve(self):
        n, x, y = list(map(int, input().split()))
        n -= 1

        lo = 0
        hi = n * max(x, y) + 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if n <= (mid // x + mid // y):
                hi = mid - 1

            else:
                lo = mid + 1

        print(lo + min(x, y))


if __name__ == "__main__":
    solution = Copies()
    solution.solve()
