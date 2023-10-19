class PerfectNumber:
    def __init__(self):
        self.start = 0
        self.head_start = 19

    def sum(self, number: int):
        sum = 0
        while number:
            sum += number % 10
            number //= 10
        return sum

    def find_next(self):
        number = self.start + self.head_start

        self.start += 100
        while self.sum(self.start + 100) > 10:
            self.start += 100
        self.head_start = 10 - self.sum(self.start)

        return number

    def find(self, k):
        number = self.find_next()
        k -= 1
        while k:
            if self.sum(number + 9) == 10:
                number += 9
            else:
                number = self.find_next()
            k -= 1

        return number

    def solve(self):
        k = int(input())
        print(self.find(k))


if __name__ == "__main__":
    solution = PerfectNumber()
    solution.solve()
