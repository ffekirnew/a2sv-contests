def main():
    n = int(input())
    answer = []
    nums = list(map(int, input().split()))

    negatives = [num for num in nums if num < 0]
    positives = [num for num in nums if num > 0]
    zeros = [num for num in nums if not num]

    if not len(positives):
        positives.append(negatives.pop())
        positives.append(negatives.pop())
    
    if len(negatives) % 2 == 0:
        zeros.append(negatives.pop())


    answer = [negatives, positives, zeros]
    
    for ans in answer:
        print(len(ans), *ans)


if __name__ == "__main__":
    main()