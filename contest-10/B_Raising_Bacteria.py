def days_it_takes(x):
    curr = 1

    while curr * 2 < x:
        curr *= 2
    
    return curr if curr * 2 != x else curr * 2

def solve():
    x = int(input())
    
    answer = 0

    while x:
        answer += 1
        x -= days_it_takes(x)
    
    print(answer)


if __name__ == "__main__":
    solve()