n, m = map( int, input().split() )
remaining = list( map( int, input().split() ) )
cost = list( map( int, input().split() ) )
indexes = [ i for i in range(1, n + 1) ]

all = [ [cost[i], remaining[i], indexes[i]] for i in range(n) ]
all.sort( key=lambda x: [x[0], x[2]] )
pos = { item[2] : index for index, item in enumerate(all) }

for _ in range(m):
    kind, amount_needed = map( int, input().split() )
    i = pos[kind]

    while amount_needed:
        remaining = all[i][1]

        if remaining >= amount_needed:
            cost = all[i][0] * amount_needed
            all[i][1] -= amount_needed
        else:
            amount_needed -= all[i][1]
            cost = all[i][0] * all[i][1]
            all[i][1] = 0
        
        i += 1 if


            

print(all, pos)