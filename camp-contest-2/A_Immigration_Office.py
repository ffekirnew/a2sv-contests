from bisect import bisect_right


n = int(input())
queue = input().split()
q = int(input())
new = [input() for _ in range(q)]

for person in new:
    print( bisect_right( queue, person ) )
