from math import inf
import sys
 
 
def solve():
    letter = sys.stdin.readline()
    
    lowers_before = [0]
    for i in range(len(letter)):
        if 'a' <= letter[i] <= 'z':
            lowers_before.append((lowers_before[-1] if i else 0) + 1)
        else:
            lowers_before.append((lowers_before[-1] if i else 0))
    
    uppers_after = [0]
    for i in range(len(letter) - 1, -1, -1):
        if 'A' <= letter[i] <= 'Z':
            uppers_after.append((uppers_after[-1] if uppers_after else 0) + 1)
        else:
            uppers_after.append((uppers_after[-1] if uppers_after else 0))
 
    uppers_after.reverse()
        
    answer = inf
    for i in range(len(letter)):
        answer = min(lowers_before[i] + uppers_after[i + 1], answer)
    
    print(answer)

if __name__ == "__main__":
    solve()