def solve():
    number_of_records = int(input())

    records = []
    after_launch = set()
    before_launch = set()
    for _ in range(number_of_records):
        type_, id = input().split()
        records.append((type_, id))

        if type_ == "+":
            after_launch.add(id)
        if type_ == "-":
            if id not in after_launch:
                before_launch.add(id)

    min_capacity = len(before_launch)
    proceedings = set()
    for type_, id in records:
        if type_ == "+":
            proceedings.add(id)
        if type_ == "-":
            if id in before_launch:
                before_launch.remove(id)
            else:
                proceedings.remove(id)

        min_capacity = max(min_capacity, len(proceedings) + len(before_launch))

    print(min_capacity)


if __name__ == "__main__":
    solve()
