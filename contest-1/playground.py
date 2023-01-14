def main():
    times = []
    n = int(input())
    for i in range(n):
        length, start = input().split()
        sequence = input()

        length = int(length) * 2
        sequence += sequence

        # find the next crossing time at each index
        g_dict = {}
        curr = None
        for i in range(length - 1, -1, -1):
            if sequence[i] == 'g':
                curr = i
            if curr == None:
                g_dict[i] = -1
            else:
                g_dict[i] = curr

        # find the actual crossing times
        time = 0
        for i, light in enumerate(sequence):
            if light == start:
                time = max(time, g_dict[i] - i)
        times.append(time)


    # print the solutions
    for time in times:
        print(time)

 
if __name__ == "__main__":
    main()