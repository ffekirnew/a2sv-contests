from collections import Counter, defaultdict


if __name__ == "__main__":
    num_of_words = int(input())
    words = []
    for test_case in range(num_of_words):
        words.append(input())

    answer = [None] * len(words[0])
    for word in words:
        for i, char in enumerate(word):
            if not answer[i]:
                answer[i] = char
            else:
                if answer[i] == '?':
                    answer[i] = char
                elif answer[i] != char and char != '?':
                    answer[i] = '!'
    
    all = Counter("abcdefghijklmnopqrstuvwxyz")
    freq = Counter(answer)

    for i, char in enumerate(answer):
        if char == '?':
            for key in all.keys():
                if key not in freq:
                    answer[i] = key
                    break
    
    for i, char in enumerate(answer):
        if char == '!':
            answer[i] = '?'
            
    answer = "".join(answer)
    print(answer)


