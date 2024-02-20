class GameShow:
    def generate_primes(self, n):
        primes = []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        i = 2
        while i <= n:
            if is_prime[i]:
                primes.append(i)
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1

        return primes

    def solve(self):
        original_k, n = list(map(int, input().split()))
        prices = list(map(int, input().split()))

        prime_set = self.generate_primes(max(prices))
        max_count = 0
        # print(prime_set)
        if len(prime_set) == 0:
            prime_set.append(1)

        for prime in prime_set:
            k = original_k
            count = 0

            for price in prices:
                if price % prime == 0:
                    count += 1
                elif k >= price:
                    count += 1
                    k -= price
                else:
                    k = 0

            max_count = max(count, max_count)

        print(max_count)


if __name__ == "__main__":
    solution = GameShow()
    solution.solve()
