import math


def formula(optimization_days, days_program_runs):
    return optimization_days + math.ceil(days_program_runs / (optimization_days + 1))

def binary_search(left, right, days_till_deadline, days_program_runs):
    while left < right:
        mid = (left + right) // 2
        if formula(mid, days_program_runs) <= days_till_deadline:
            return True
        else:
            left = mid + 1

    return False

def solve():
    tests = int(input())
    for _ in range(tests):
        days_till_deadline, days_program_runs = map(int, input().split())
        can_be_done = binary_search(0, days_till_deadline, days_till_deadline, days_program_runs)
        print("YES" if can_be_done else "NO")


if __name__ == "__main__":
    solve()