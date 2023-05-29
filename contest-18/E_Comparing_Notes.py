def solve():
    aklile_notes = input()
    betty_notes = input()

    shorter = 0 if min(len(aklile_notes), len(betty_notes)) else 1
    
    for index in range(min(len(aklile_notes), len(betty_notes))):
        if aklile_notes[index] == '-' or betty_notes[index] == '-':
            print("YES")
            return
        
        elif aklile_notes[index] != betty_notes[index]:
            print("NO")
            return
    
    notes = [aklile_notes, betty_notes]
    if not '-' in notes[shorter]:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    solve()