from collections import Counter
import heapq


def solve():
    n, k = list(map(int, input().split()))
    s = list(map(int, input().split()))

    freq_s = Counter(s)

    real_list = [(-count, number, 0) for number, count in freq_s.items()]
    real_list.sort(key=lambda x: x[0])
    
    t = []
    while k:
        count, element, used = heapq.heappop(real_list)
        t.append(element)
        if count != 0:
            to_be_used_again = (-(freq_s[element] // (used + 2)), element, used + 1)
            heapq.heappush(real_list, to_be_used_again)
        k -= 1

    print(*t)
    

if __name__ == "__main__":
    solve()