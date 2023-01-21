if __name__ == "__main__":
    n = int(input())
    answers = []
    for i in range(n):
        test = list(map(int, input().split()))
        test.sort()
        answers.append(test[1])
    
    for ans in answers:
        print(ans)