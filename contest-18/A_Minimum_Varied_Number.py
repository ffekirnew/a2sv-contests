def solve():
    tests = int(input())
    for _ in range(tests):
        number = int(input())
        answer = []
        used = set()
        
        while number:
            for i in range(9, 0, -1):
                if number >= i and i not in used:
                    used.add(i)
                    answer.insert(0, str(i))
                    number -= i
        
        print("".join(answer))

if __name__ == "__main__":
    solve()