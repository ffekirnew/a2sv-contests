class EligibleTeams:
    def solve(self):
        tests = int(input())
        for _ in range(tests):
            n, x = list(map(int, input().split()))
            arr = list(map(int, input().split()))

            arr.sort()
            teams = 0
            currTeamSize = 0

            for i in range(n - 1, -1, -1):
                if arr[i] >= x:
                    teams += 1
                    currTeamSize = 0
                elif arr[i] * (currTeamSize + 1) >= x:
                    teams += 1
                    currTeamSize = 0
                else:
                    currTeamSize += 1
            
            print(teams)


if __name__ == "__main__":
    solution = EligibleTeams()
    solution.solve()