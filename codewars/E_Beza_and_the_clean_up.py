class BezeAndTheCleanUp:
    def solve(self):
        (
            number_of_a_weighing_trash,
            number_of_b_weighing_trash,
            weight_limit,
            weight_a,
            weight_b,
        ) = list(map(int, input().split()))

        def get_number_of_b_that_can_be_accomodated(total_a_weight):
            return min(
                (weight_limit - total_a_weight) // weight_b, number_of_b_weighing_trash
            )

        a_weighing_trash = list(map(int, input().split()))
        b_weighing_trash = list(map(int, input().split()))

        a_weighing_trash.sort(reverse=True)
        b_weighing_trash.sort(reverse=True)

        b_prefix_sum = [0]
        for number in b_weighing_trash:
            b_prefix_sum.append(b_prefix_sum[-1] + number)

        a_value_sum = 0
        max_value = b_prefix_sum[get_number_of_b_that_can_be_accomodated(0)]
        for index in range(number_of_a_weighing_trash):
            a_value_sum += a_weighing_trash[index]

            total_a_weight = (index + 1) * weight_a
            if total_a_weight > weight_limit:
                break

            number_of_b_that_can_be_accomodated = min(
                (weight_limit - total_a_weight) // weight_b, number_of_b_weighing_trash
            )
            max_value = max(
                max_value,
                b_prefix_sum[get_number_of_b_that_can_be_accomodated(total_a_weight)]
                + a_value_sum,
            )
        print(max_value)


if __name__ == "__main__":
    solution = BezeAndTheCleanUp()
    solution.solve()
