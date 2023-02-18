num_topics = int(input())
teacher =  list(map(int, input().split()))
students =  list(map(int, input().split()))

all = [ teacher[i] - students[i] for i in range(num_topics) ]

teacher = None
students = None

all.sort(reverse=True)
freq = {}

for i in range(len(all)):
    if all[ i ] < 0:
        break
    freq[all[i]] = len(all) - i

num = 0

good = 0

print(freq)

for i in range(len(all)):
    if all[i] < 1:
        break
    
    if (-1 * all[i]) in freq:
        good += freq[all[i]] - 1 - freq[-1 * all[i]]
    else:
        good += freq[all[i]] - 1

print(good)