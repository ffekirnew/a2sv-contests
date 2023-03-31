def solve():
    magic_number = (2 ** 31 - 1)
    lines = int(input())
    ops = [input() for _ in range(lines)]

    x = 0
    in_for_loop = []

    for op in ops:
        if op[0] == 'f':
            new_loop = (in_for_loop[-1][0] if in_for_loop else 1) * int(list(op.split())[1])
            minimum = min(new_loop, magic_number)

            in_for_loop.append([minimum, new_loop == minimum])
        elif op[0] == 'a':
            if in_for_loop:
                if (in_for_loop[-1][0] == magic_number - x and not in_for_loop[-1][1]) or (in_for_loop[-1][0] > magic_number):
                    print("OVERFLOW!!!")
                    return

                x += in_for_loop[-1][0]              
            else:
                x += 1

        else:
            in_for_loop.pop()
    print(x)
    return

if __name__ == "__main__":
    solve()