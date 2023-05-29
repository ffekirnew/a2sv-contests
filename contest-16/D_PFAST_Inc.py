from collections import defaultdict

def solve():
    n_and_m = list(map(int, input().split()))
    n, m = n_and_m[0], n_and_m[1] if len(n_and_m) == 2 else 0

    vertices = [input() for _ in range(n)]

    enemies = defaultdict(lambda: defaultdict(bool))
    for _ in range(m):
        name1, name2 = input().split()
        enemies[name1][name2] = True
        enemies[name2][name1] = True
    
    subsets = set()
    def backtrack(index, curr_subset):
        if index == len(vertices):
            subsets.add(tuple(curr_subset))

        for i in range(index, len(vertices)):
            can_do = True
            for node in curr_subset:
                if enemies[vertices[i]][node]:
                    can_do = False
                    break
            if can_do:
                backtrack(i + 1, curr_subset + [vertices[i]])
            backtrack(i + 1, curr_subset + [])
    
    backtrack(0, [])
    answer = []
    for subset in subsets:
        no_enemies = True

        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if enemies[subset[i]][subset[j]]:
                    no_enemies = False
                    break
        
        if no_enemies and len(subset) > len(answer):
            answer = subset

    answer = list(answer)
    answer.sort()
    print(len(answer))
    for name in answer:
        print(name)


if __name__ == "__main__":
    solve()
