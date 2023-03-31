tests = int(input())

for _ in range(tests):
    n, m = map( int, input().split() )
    dividers = list( map( int, input().split() ) )

    dividers.sort()

    curr = 2

    while dividers and n > curr:
        curr -= 1
        curr += dividers.pop()

    if curr >= n:
        print( m - len(dividers) )
    else:
        print(-1)
