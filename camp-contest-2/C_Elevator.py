tests = int(input())

for _ in range(tests):
    walk_time, elevator_time, curr_floor = map( int, input().split() )
    answer = float('inf')

    for floor in range(5):
        she_going_up = walk_time * ( floor )
        elevator_coming_down = elevator_time * abs( curr_floor - floor ) if floor < 4 else 0
        elevator_going_up = elevator_time * (4 - floor) if floor < 4 else 0
        answer = min( she_going_up + elevator_coming_down + elevator_going_up, answer)
    
    print(answer)