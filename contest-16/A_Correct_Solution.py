import heapq

def solve():
    number = list(input())
    heapq.heapify(number)

    answer = list(input())

    minimized = []
    while number:
        minimized.append(heapq.heappop(number))

    i = 0
    while i < len(minimized) and minimized[i] == '0':
        i += 1
    
    if i < len(minimized):
        minimized[i], minimized[0] = minimized[0], minimized[i]

    if answer == minimized:
        print('OK')
    else:
        print('WRONG_ANSWER')

if __name__ == "__main__":
    solve()


