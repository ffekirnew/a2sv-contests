from collections import deque


def solve():
    string = input()

    answer = []

    closings_index = deque()
    for i, char in enumerate(string):
        if char == ')':
            closings_index.append(i)
    
    i = 0
    while closings_index:
        openings_index = deque([])
        while i < closings_index[0]:
            if string[i] == '(':
                openings_index.append(i)
            i += 1

        if openings_index:
            answer.append([])

        while openings_index and closings_index and openings_index[0] < closings_index[0]:
            answer[-1].append(openings_index.popleft() + 1)
            answer[-1].append(closings_index.popleft() + 1)
        else:
            if closings_index:
                closings_index.popleft()
    
    print(len(answer))
    for ans in answer:
        ans.sort()
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    solve()