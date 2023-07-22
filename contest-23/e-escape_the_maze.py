import sys
import threading

def solve():
    tests = int(input())
    for _ in range(tests):
        num_rooms, num_friends = map(int, input().split())


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()
