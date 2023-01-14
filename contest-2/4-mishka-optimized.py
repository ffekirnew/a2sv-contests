from collections import Counter, defaultdict
"""Does something."""

if __name__ == "__main__":
    duration, k = list(map(int, input().split()))
    theorems = list(map(int, input().split()))
    behavior = list(map(int, input().split()))

    answer = 0
    written = 0
    for i, theorem in enumerate(theorems):
        if behavior[i] == 1:
            written += theorem
        else:
            pass

    print(answer + written)
