from collections import defaultdict


def main():
    n = int(input())
    answer = []

    for i in range(n):
        board = []
        input()
        for i in range(8):
            board.append(list(input()))

        for row in range(8):
            for col in range(8):
                if board[row][col] == "#":
                    adj = [[row - 1, col - 1], [row - 1, col + 1], [row + 1, col - 1], [row + 1, col + 1]]

                    flag = True
                    for a in adj:
                        if a[0] < 0 or a[1] < 0 or a[0] > 7 or a[1] > 7:
                            flag = False
                            break
                        elif board[a[0]][a[1]] != '#':
                            flag = False
                            break
                    
                    if flag:
                        answer.append([row + 1, col + 1])

    
    for ans in answer:
        print(*ans)


if __name__ == "__main__":
    main()