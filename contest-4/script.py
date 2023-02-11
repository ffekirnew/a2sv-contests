strings = list(map(str, [303340053, 301383642, 339600795, 371353217, 261982227, 417569077]))

print(strings)

for string in strings:
    for i in range(0, len(string), 3):
        print(string[i:i+3], end=" ")
    print()