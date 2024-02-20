class MeetingOnTheLine:
    def solve(self):
        tests = int(input())
        for _ in range(tests):
            n = int(input())
            positions = list(map(int, input().split()))
            ready_times = list(map(int, input().split()))

            if n == 1:
                print((sum(positions) - sum(ready_times) / (n - 1)))


if __name__ == "__main__":
    solution = MeetingOnTheLine()
    solution.solve()