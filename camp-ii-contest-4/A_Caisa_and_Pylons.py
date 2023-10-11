class CasiaAndPylons:
    def solve(self):
        n = int(input())
        heights = list(map(int, input().split()))

        min_money = heights[0]
        curr_energy = 0

        for i in range(len(heights) - 1):
            if curr_energy + heights[i] < heights[i + 1]:
                min_money += heights[i + 1] - heights[i] - curr_energy
                curr_energy = 0
            else:
                curr_energy += heights[i] - heights[i + 1]

        print(min_money)


if __name__ == "__main__":
    solution = CasiaAndPylons()
    solution.solve()
