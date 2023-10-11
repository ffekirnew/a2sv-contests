class MultiplicationTable:
    def solve(self):
        def count_less_equal(number: int, rows: int, cols: int):
            count = 0
            for i in range(1, rows + 1):
                count += min(number // i, cols)
            return count

        n, m, k = map(int, input().split())
        left, right = 1, n * m

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid, n, m) < k:
                left = mid + 1
            else:
                right = mid

        print(left)


if __name__ == "__main__":
    solution = MultiplicationTable()
    solution.solve()
