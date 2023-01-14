from collections import Counter
def main():
    n = int(input())
    names = [name for name in input().split()]
    flaged_bad = set([bad for bad in input().split()])
    answer = 0
    for name in names:
        freq = Counter(name)
        excellent = True
        instance = None
        for value in freq.values():
            if not instance:
                instance = value
            elif value != instance:
                excellent = False
                break
        if excellent and name not in flaged_bad:
            answer += 1
    print(answer)

 
if __name__ == "__main__":
    main()