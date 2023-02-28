n, m = map( int, input().split() )
remaining = list( map( int, input().split() ) )
cost = list( map( int, input().split() ) )
indexes = [ i for i in range(1, n + 1) ]

all = [ [cost[i], remaining[i], indexes[i]] for i in range(n) ]
all.sort( key=lambda x: [x[0], x[2]] )
pos = { item[2] : index for index, item in enumerate(all) }

for _ in range(m):
    kind, amount = map( int, input().split() )
    cost = 0
    while amount:
        if all[ pos[ kind ] ][1] >= amount:
            cost += all[ pos[ kind ] ][0] * amount
            all[ pos[ kind ] ][1] -= amount
        else:
            

print(all, pos)