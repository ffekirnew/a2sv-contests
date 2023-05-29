import sys
import threading

def solve():
    pass

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()
