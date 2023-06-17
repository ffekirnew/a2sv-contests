import sys
import threading

def solve():
    # accept input with sys
    string = sys.stdin.readline()

    if 'm' in string or 'w' in string:
        print(0)
        return
    
    memo = {}
    nn_before, uu_before = set(), set()

    def ways_to_decode(index):
        if index >= len(string):
            return 1

        if index in memo:
            return memo[index]
        
        if index + 1 < len(string) and string[index] == string[index + 1] == 'n':
            memo[index] = 2 * ways_to_decode(index + 1)
            if index + 1 in nn_before:
                memo[index] -= 1
            nn_before.add(index)
                
        elif index + 1 < len(string) and string[index] == string[index + 1] == 'u':
            memo[index] = 2 * ways_to_decode(index + 1)
            if index + 1 in uu_before:
                memo[index] -= 1
            uu_before.add(index)

        else:
            memo[index] = ways_to_decode(index + 1)
        
        return memo[index]

    print(ways_to_decode(0) % (10**9 + 7))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 30)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()
