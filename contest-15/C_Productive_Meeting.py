import heapq
def solve():
    tests = int(input())
    for _ in range(tests):
        num_people = int(input())
        sociability = list(map(lambda x: -int(x), input().split()))
        sociability = [[value, i] for i, value in enumerate(sociability)]

        heapq.heapify(sociability)

        talks = []

        while True:
            person_1 = heapq.heappop(sociability)
            person_2 = heapq.heappop(sociability)

            if person_1[0] == 0 or person_2[0] == 0:
                break

            talks.append([person_1[1] + 1, person_2[1] + 1])
            
            person_1[0] += 1
            person_2[0] += 1
            
            heapq.heappush(sociability, person_1)
            heapq.heappush(sociability, person_2)
        
        print(len(talks))
        for talk in talks:
            print(*talk)

if __name__ == "__main__":
    solve()
