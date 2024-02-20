class Giveaway:
    def solve(self):
        n, q = list(map(int, input().split()))
        prices = list(map(int, input().split()))
        prices.sort()
        prefix_sum = [0]
        for number in prices:
            prefix_sum.append(prefix_sum[-1] + number)

        for _ in range(q):
            x, y = list(map(int, input().split()))

            left = n - x
            right = left + y

            print(prefix_sum[right] - prefix_sum[left])


if __name__ == "__main__":
    solution = Giveaway()
    solution.solve()