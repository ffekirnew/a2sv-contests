from math import inf

tests = int( input() )
answers = []
for test in range(tests):
    n, m = map( int, input().split() )
    states = list(input())

    # find ones to the right
    ones_to_right = [0] * n

    last = inf
    for i in range(n - 1, -1, -1):
        ones_to_right[i] = last
        if states[i] == "1":
            last = i
    
    # find ones to the left 
    ones_to_left = [0] * n

    last = -inf
    for i in range(n):
        ones_to_left[i] = last
        if states[i] == "1":
            last = i
    
    # print(ones_to_left, ones_to_right)

    for i in range(n):
        if states[i] == "0":
            left_one, right_one = i - ones_to_left[i], ones_to_right[i] - i
            if left_one == right_one:
                continue
            else:
                closest_one = min( left_one, right_one )
                if closest_one <= m:
                    states[i] = "1"

    # for i in range(n):
    #     if states[i] == "1":
    #         states[i] = 'a'
    
    # save_range = 0
    # for i in range(n):
    #     if states[i] == 'a':
    #         save_range = m
    #     elif save_range:
    #         states[i] = '1'
    #         save_range -= 1

    # save_range = 0
    # for i in range(n - 1, -1, -1):
    #     if states[i] == 'a':
    #         save_range = m
    #     elif save_range:
    #         if states[i] == '1' and (i > 0 and states[i - 1] == 'a') and (save_range == m):
    #             states[i] = '0'
    #         else:
    #             states[i] = '1'
    #         save_range -= 1

    # for i in range(n):
    #     if states[i] == 'a':
    #         states[i] = '1'
    
    answers.append("".join(states))

for ans in answers:
    print(ans)
                