n, a, b = map( int, input().split() )
solved = list( map( int, input().split() ) )

sub_arrays_less_than_equal_b = 0
l = 0
sum_ = 0
for r in range(n):
    sum_ += solved[r]
    while sum_ > b:
        sum_ -= solved[l]
        l += 1
    sub_arrays_less_than_equal_b += r - l + 1


sub_arrays_less_than_a = 0
l = 0
sum_ = 0
for r in range(n):
    sum_ += solved[r]
    while sum_ >= a:
        sum_ -= solved[l]
        l += 1
    sub_arrays_less_than_a += r - l + 1


print(sub_arrays_less_than_equal_b - sub_arrays_less_than_a)