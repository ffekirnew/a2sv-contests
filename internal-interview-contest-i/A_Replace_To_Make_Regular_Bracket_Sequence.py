def solve():
    opening_of = { '}': '{', ')': '(', '>': '<', ']': '[' }

    stack = []
    sequence = input()

    replacements = 0
    for char in sequence:
        if char  in opening_of:
            if not stack:
                print("Impossible")
                return

            replacements += int(opening_of[char] != stack[-1])
            stack.pop()

        else:
            stack.append(char)

    if not stack:
        print(replacements)
    else:
        print("Impossible")
        

if __name__ == "__main__":
    solve()