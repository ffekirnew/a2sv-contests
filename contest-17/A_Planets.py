from collections import Counter

def solve():
    tests = int(input())
    for _ in range(tests):
        n, c = list(map(int, input().split()))
        orbits = list(map(int, input().split()))

        planets = Counter(orbits)

        answer = 0
        for key, value in planets.items():
            if value < c:
                answer += value
            else:
                answer += c
        
        print(answer)

if __name__ == "__main__":
    solve()