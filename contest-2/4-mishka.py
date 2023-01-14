from collections import Counter, defaultdict


if __name__ == "__main__":
    duration, k = list(map(int, input().split()))
    theorems = list(map(int, input().split()))
    behavior = list(map(int, input().split()))

    # find prefix sum
    p = [0]
    for i, theorem in enumerate(theorems):
        if not behavior[i]:
            p.append(p[-1])
        else:
            p.append(p[-1] + theorem)

    # find suffix sum
    s = [0]
    for j in range(len(theorems) - 1, -1, -1):
        theorem = theorems[j]
        if not behavior[j]:
            s.append(s[-1])
        else:
            s.append(s[-1] + theorem)
    s.reverse()

    # set up the sliding window
    i, j = 0, k - 1
    curr_sum = sum(theorems[i:j + 1])
    answer = curr_sum + s[j + 1]
    j += 1
    i += 1
    while j < len(theorems):
        curr_sum -= theorems[i - 1]
        curr_sum += theorems[j]
        answer = max(answer, p[i] + s[j + 1] + curr_sum)
        i += 1
        j += 1

    print(answer)

