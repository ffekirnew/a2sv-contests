class ToAddOrNotToAdd:
    def solve(self):
        n, m = list(map(int, input().split()))
        array = list(map(int, input().split()))

        array.sort()

        max_occurrences = 0
        max_occurrences_num = None

        left = 0
        running_sum = 0
        for right in range(n):
            running_sum += array[right]
            while (running_sum + m) // (right - left + 1) < array[right]:
                running_sum -= array[left]
                left += 1

            # print(array[right], left, right)
            if right - left + 1 > max_occurrences:
                max_occurrences = right - left + 1
                max_occurrences_num = array[right]

        print(max_occurrences, max_occurrences_num)


if __name__ == "__main__":
    solution = ToAddOrNotToAdd()
    solution.solve()
