tests = int( input() )
operations = []

for test in range(tests):
    rooms = int(input())
    evilness = list( map( int, input().split() ) )

    i = 0
    ops = 0

    while i < rooms - 1:
        if evilness[i] == 0: i += 1
        else: break
    
    while i < rooms - 1:
        ops += evilness[i] if evilness[i] else 1
        i += 1
    
    operations.append(ops)

for op in operations:
    print(op)