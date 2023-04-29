from collections import defaultdict, deque


def solve():
    reposts = int(input())
    events = [list(input().split()) for _ in range(reposts)]
    events = [ [event[0].lower(), event[2].lower()] for event in events ]

    graph = defaultdict(list)

    for from_, to_ in events:
        graph[to_].append(from_)
    
    max_length = [0]

    fringe = deque()
    visited = set()

    fringe.append(("polycarp", ["polycarp"]))

    while fringe:
        curr_state, curr_path = fringe.popleft()

        if curr_state not in graph:
            max_length[0] = max(max_length[0], len(curr_path))

        if curr_state not in visited:
            visited.add(curr_state)
            for state in graph[curr_state]:
                fringe.append((state, curr_path + [state]))

    print(max_length[0])


if __name__ == "__main__":
    solve()