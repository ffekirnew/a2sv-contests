from collections import defaultdict


if __name__ == "__main__":
    number_of_test_cases = int(input())
    scores = list(map(int, input().split()))

    # find prefix sum
    prefix = []
    for score in scores:
        if not prefix:
            prefix.append(score)
        else:
            prefix.append(prefix[-1] + score)
    answers = []
    max_score = scores[0]
    min_score = scores[0]
    amazing = 0
    for i in range(1, len(scores)):
        if scores[i] > int(prefix[i - 1] / i) and scores[i] > max_score:
            amazing += 1
        elif scores[i] < int(prefix[i] / i) and scores[i] < min_score:
            amazing += 1
        max_score = max(max_score, scores[i])
        min_score = min(min_score, scores[i])

    print(amazing)


