from math import inf


class LilaAndThePlaylist:
    def solve(self):
        n, p = list(map(int, input().split()))
        positivity = list(map(int, input().split()))
        answer = [0, inf]

        prefix_sum = [0]
        for number in positivity:
            prefix_sum.append(prefix_sum[-1] + number)
        
        listened_to = 0
        if p > prefix_sum[-1]:
            listened_to = (p // prefix_sum[-1]) * n
            p %= prefix_sum[-1]

        for number in positivity:
            prefix_sum.append(prefix_sum[-1] + number)
        for index, positivity in enumerate(prefix_sum):
            if positivity >= p:
                lo, hi = 1, index - 1

                while lo <= hi:
                    mid = lo + (hi - lo) // 2

                    if positivity - prefix_sum[mid] >= p:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                
                if index - lo + 1 < answer[1]:
                    answer = [lo, index - lo + 1]
        
        print(answer[0], answer[1] + listened_to)



if __name__ == "__main__":
    solution = LilaAndThePlaylist()
    solution.solve()