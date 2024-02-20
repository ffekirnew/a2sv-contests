class TsegasTriangle:
    def solve(self):
        n, number_of_operations = list(map(int, input().split()))
        bottom_row = list(map(int, input().split()))

        range_sum = [0] * (n + 1)

        for _ in range(number_of_operations):
            left, right, value = list(map(int, input().split()))

            range_sum[left] -= value
            range_sum[right + 1] += value
        
        print(range_sum)
        prefix_sum = [0]
        for number in range_sum:
            prefix_sum.append(prefix_sum[-1] + number)
        
        print(prefix_sum)
            


if __name__ == "__main__":
    solution = TsegasTriangle()
    solution.solve()