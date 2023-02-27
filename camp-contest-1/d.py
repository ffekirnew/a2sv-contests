from collections import defaultdict

n, k, q = map( int, input().split() )
recipies = [ list(map( int, input().split() )) for i in range(n) ]

# find the permissibility of each temp in the 
min_start, max_end = [recipies[0][0], recipies[0][1]]

for recipe in recipies:
    min_start = min( min_start, recipe[0] )
    max_end = max( max_end, recipe[1] )

freq = defaultdict(int)

for recipe in recipies:
    freq[ recipe[0] ] += 1
    freq[ recipe[1] + 1 ] -= 1

# do the prefix sum
running_sum = 0

for temp in range(min_start, max_end + 1):
    freq[ temp ] += running_sum
    running_sum = freq[temp]

# print(freq)

greater_than_k = 0

for temp in range(min_start, max_end + 1):
    freq[ temp ] = 1 if freq[temp] >= k else 0
    freq[ temp ] += greater_than_k
    greater_than_k = freq[ temp ]

del freq[max_end + 1]

for i in range(q):
    l, r = map(int, input().split())
    left = freq[l - 1] if l - 1 <= max_end else freq[ max_end ]
    right = freq[r] if r <= max_end else freq[ max_end ]
    print(right - left)
