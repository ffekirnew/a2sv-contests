def main():
    # create the object to be returned
    times = []

    # accept the first input
    n = int(input())
    for i in range(n):
        # accpet the inputs of the test cases
        length, start = input().split()
        sequence = input()

        # since it is circular, double the light sequence and length
        length = int(length) * 2
        sequence += sequence

        # find the next crossing time at each index
        next_g = {}
        curr = None
        for i in range(length - 1, -1, -1):
            if sequence[i] == 'g':
                curr = i
            if curr == None:
                next_g[i] = -1
            else:
                next_g[i] = curr

        # find the actual crossing times
        time = 0
        for i, light in enumerate(sequence):
            if light == start:
                time = max(time, next_g[i] - i)
        times.append(time)


    # print the solutions
    for time in times:
        print(time)

 
if __name__ == "__main__":
    main()