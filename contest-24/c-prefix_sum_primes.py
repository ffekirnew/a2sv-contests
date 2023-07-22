import sys
import threading

primes = {1: False, 2: True}
def is_prime(n):
    if n not in primes:
        set_ = False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                primes[n] = False
                set_ = True
                break
        if not set_:
            primes[n] = True
            
    return primes[n]

def count_prime_prefixes(array):
    count = 0
    running_sum = 0
    for i in range(len(array)):
        running_sum += array[i]
        if is_prime(running_sum):
            count += 1
    
    return count

def solve():
    n = int(input())
    tiles = list(map(int, input().split()))
    number_of_ones = tiles.count(1)
    number_of_twos = tiles.count(2)


    best = [None]
    best_count = [0]
    memo = {}
    def permutations(array, ones_left, twos_left):
        if (ones_left, twos_left) in memo:
            return
        
        memo[(ones_left, twos_left)] = True
        if ones_left == 0 and twos_left == 0:
            # count the prime prefixes of this array
            count = count_prime_prefixes(array)
            
            if not best[0] or count > best_count[0]:
                best_count[0] = count
                best[0] = array
        
        if ones_left:
            permutations(array + [1], ones_left - 1, twos_left)
        if twos_left:
            permutations(array + [2], ones_left, twos_left - 1)
    
    permutations([], number_of_ones, number_of_twos)
    print(*best[0])

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
solution_thread = threading.Thread(target = solve)
solution_thread.start()
solution_thread.join()
