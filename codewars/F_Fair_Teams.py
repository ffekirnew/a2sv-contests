class FairTeams:
    def solve(self):
        n = int(input())
        skills = list(map(int, input().split()))

        print(max(skills) - min(skills) // n)


if __name__ == "__main__":
    solution = FairTeams()
    solution.solve()