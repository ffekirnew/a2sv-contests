def solve():
    MAGIC_NUMBER = (2 ** 31 - 1)

    lines = int(input())

    stack = [1]
    x = 0

    for _ in range(lines):
        op = input()

        if op.startswith("for"):
            new_iterations = int(op.split(" ")[1])
            stack.append( min(stack[-1] * new_iterations, MAGIC_NUMBER + 1) )

        elif op == "add":
            x += stack[-1]

            if x > MAGIC_NUMBER:
                print("OVERFLOW!!!")
                return
            
        else:
            stack.pop()
    
    print(x)

if __name__ == "__main__":
    solve()