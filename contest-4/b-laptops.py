def check_if_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


number_of_laptops = int(input())
laptops = []
for i in range(number_of_laptops):
    laptops.append(list(map(int, input().split())))

laptops.sort()

perfomances = [perf for price, perf in laptops]


if check_if_sorted(perfomances):
    print("Poor Alex")
else:
    print("Happy Alex")