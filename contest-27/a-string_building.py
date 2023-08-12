def solve():
    tests = int(input())
    for _ in range(tests):
        s = input()
        options = ["aa", "aaa", "bbb", "bb"]


        def check(start, end, option):
            if end > len(s):
                return False

            o_i = 0
            for i in range(start, end):
                if option[o_i] != s[i]:
                    return False
                o_i += 1
            
            return True
        
        memo = {len(s) : True}
        def dp(i):
            if i not in memo:
                memo[i] = False
                for option in options:
                    if check(i, i + len(option), option):
                        memo[i] |= dp(i + len(option))
            
            return memo[i]
    
        print("YES" if dp(0) else "NO")


if __name__ == "__main__":
    solve()

