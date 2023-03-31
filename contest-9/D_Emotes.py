"""
The Seven Steps:
1. Understand the problem?
2. Solve the problem manually?
3. Come up with a solution idea on paper?
4. Play devil’s advocate against your idea before falling in love with it?
5. The implementation, that is our mission, Touche?
6. Comprehensive test cases?
7. Simplify and clean up your code?
"""

def solve():
    n, m, k = list(map(int, input().split()))
    emotes = list(map(int, input().split()))

    emotes.sort()

    use_other = m // (k + 1)
    use_main = m - use_other

    print(use_main * emotes[-1] + use_other * emotes[-2])

if __name__ == "__main__":
    solve()