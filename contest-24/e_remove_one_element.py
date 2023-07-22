from typing import List

def solve():
    n = int(input())
    array = list(map(int, input().split()))

    memo = {}
    max_length = 0
    def top_down(starting_index, index, removed):
        if (starting_index, index, removed) in memo:
            return memo[(starting_index, index, removed)]
        else:
            if index == len(array):
                return 0
            else:
                if index > starting_index and array[index] > array[index - 1]:
                    if not removed:
                        top_down(starting_index, index + 1, True)
                    top_down(index, index + 1, removed)
                else:
                    top_down(starting_index, index + 1, removed)
                    
                
        
    print(top_down(0, 0, False))


if __name__ == "__main__":
    solve()