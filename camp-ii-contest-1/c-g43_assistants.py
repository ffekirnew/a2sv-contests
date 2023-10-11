import heapq


def solve():
    tests = int(input())
    for _ in range(tests):
        number_of_students = int(input())
        assistance_times = []

        for _ in range(number_of_students):
            heapq.heappush(assistance_times, list(map(int, input().split())))

        end_queue = []
        max_assistants = 0
        assistants_needed = 0
        while assistance_times:
            start, end = heapq.heappop(assistance_times)
            while end_queue and end_queue[0] <= start:
                heapq.heappop(end_queue)
                assistants_needed -= 1

            assistants_needed += 1
            heapq.heappush(end_queue, end)

            max_assistants = max(max_assistants, assistants_needed)

        print(max_assistants)


if __name__ == "__main__":
    solve()
