from math import inf


class SaveThaMagazines:
    def solve(self):
        tests = int(input())
        for _ in range(tests):
            saved = 0
            number_of_boxes = int(input())
            is_covered = list(map(int, input()))
            books = list(map(int, input().split()))
            left = 0
            running_sum = 0
            no_lid_count = 0
            for right in range(number_of_boxes):
                if is_covered[right]:
                    running_sum += books[right]
                    continue
                if right == 0:
                    running_sum = books[right]
                    no_lid_count = 1
                    continue
                if right > 0 and not is_covered[right - 1]:
                    while no_lid_count > 0:
                        running_sum -= books[left]
                        left += 1
                        no_lid_count -= 1
                    running_sum += books[right]
                    no_lid_count += 1
                if right > 0 and is_covered[right - 1]:
                    min1, min2 = inf, inf
                    for i in range(left, right):
                        if books[i] <= min1:
                            min2, min1 = min1, books[i]
                        if books[i] <= min2:
                            min2 = books[i]
                    if no_lid_count == 0:
                        saved += running_sum
                    elif no_lid_count == 1:
                        saved += running_sum - min1
                    else:
                        saved += running_sum - min1 - min2
                    running_sum = books[right]
                    no_lid_count = 1
                    left = right
            if no_lid_count != right - left + 1:
                min1, min2 = inf, inf
                for i in range(left, right + 1):
                    if books[i] <= min1:
                        min2, min1 = min1, books[i]
                    if books[i] <= min2:
                        min2 = books[i]
                if no_lid_count == 0:
                    saved += running_sum
                elif no_lid_count == 1:
                    saved += running_sum - min1
                else:
                    saved += running_sum - min1 - min2

            print(saved)


if __name__ == "__main__":
    solution = SaveThaMagazines()
    solution.solve()
