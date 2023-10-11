from collections import defaultdict
from typing import Dict


class PerfectKeyboard:
    def build_graph(self, password: str):
        graph = defaultdict(set)
        degree = defaultdict(int)
        for i in range(len(password) - 1):
            if password[i + 1] in graph[password[i]]:
                continue

            graph[password[i]].add(password[i + 1])
            graph[password[i + 1]].add(password[i])
            degree[password[i]] += 1
            degree[password[i + 1]] += 1
            if len(graph[password[i]]) > 2 or len(graph[password[i + 1]]) > 2:
                return None, None
        return graph, degree

    def determine_starting(self, password: str, degree: Dict):
        starting = None
        degree_1_count = 0
        for char in password:
            if degree[char] == 1:
                starting = char
                degree_1_count += 1

        return starting if degree_1_count > 1 else None

    def test_case(self, password: str):
        if len(password) == 1:
            print("YES")
            print("e" + "".join([
                    chr(char)
                    for char in range(ord("a"), ord("z") + 1)
                    if chr(char) != password
                ]))

        graph, degree = self.build_graph(password)
        if graph is None:
            print("NO")
            return

        starting = self.determine_starting(password, degree)
        if starting is None:
            print("NO")
            return

        answer = []
        visited = set()
        stack = [starting]
        while stack:
            node = stack.pop()
            if node in visited:  # cycle detected
                print("NO")
                return

            visited.add(node)
            answer.append(node)
            for child in graph[node]:
                graph[child].remove(node)
                stack.append(child)

        print("YES")
        print(
            "".join(
                answer
                + [
                    chr(char)
                    for char in range(ord("a"), ord("z") + 1)
                    if chr(char) not in visited
                ]
            )
        )

    def solve(self):
        tests = int(input())
        for _ in range(tests):
            password = input()
            self.test_case(password)


if __name__ == "__main__":
    solution = PerfectKeyboard()
    solution.solve()

