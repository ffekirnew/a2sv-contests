days, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(m) ]

all_days = [0] * (days + 1)

for avail in arr:
    all_days[avail[0]] += 1
    all_days[avail[1] + 1] -= 1

if all_days[0] == 0:
    print("YES")
    exit()

for i in range(1, days):
    all_days[i] += all_days[i - 1]

    if all_days[i] == 0:
        print("YES")
        exit()

print("NO")
exit()