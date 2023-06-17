def solve():
    n = int(input())
    activities = list(map(int, input().split()))
    count = [0]
    memo = {}
    
    def dp(day, last_activity):
        count[0] += 1

        if day == n:
            return 0
        
        if (day, last_activity) in memo:
            return memo[(day, last_activity)]
        
        if activities[day] == 0:
            memo[(day, last_activity)] = 1 + dp(day + 1, 0)
        
        elif activities[day] == 1:
            memo[((day, last_activity))] =  1 + dp(day + 1, 0) if last_activity == 1 else dp(day + 1, 1)

        elif activities[day] == 2:
            memo[(day, last_activity)] = 1 + dp(day + 1, 0) if last_activity == 2 else dp(day + 1, 2)

        else:
            if last_activity == 0:
                memo[(day, last_activity)] = min(dp(day + 1, 1), dp(day + 1, 2))
            else:
                memo[(day, last_activity)] = min( 1 + dp(day + 1, last_activity), dp(day + 1, 3 - last_activity))
        
        return memo[(day, last_activity)]
    
    print(dp(0, -1))

if __name__ == "__main__":
    solve()
