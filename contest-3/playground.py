from collections import defaultdict


def main():
    num_of_tests = int(input())
    answer = []

    for i in range(num_of_tests):
        answer.append(0)
        grid = []
        n = int(input())

        for i in range(n):
            grid.append(list(input()))
        
        seen = set()
        for row in range(n):
            for col in range(n):
                if tuple([row, col]) in seen:
                    pass
                else:
                    places = []
                    zeros_ones = {'0': 0, '1': 1}

                    places.append(tuple([row, col]))
                    places.append(tuple([n - row - 1, col]))
                    places.append(tuple(reversed(places[0])))
                    places.append(tuple(reversed(places[1])))
                    
                    for p in places:
                        zeros_ones[grid[p[0]][p[1]]] += 1
                        seen.add(p)
                    
                    answer[-1] += min(list(zeros_ones.values()))
    
    for ans in answer:
        print(ans)


if __name__ == "__main__":
    main()