class SumInBinaryTree:
    def solve(self):
        tests = int(input())
        for _ in range(tests):
            n = int(input())

            answer = n
            while n > 1:
                answer += n // 2
                n //= 2
            
            print(answer)


if __name__ == "__main__":
    solution = SumInBinaryTree()
    solution.solve()