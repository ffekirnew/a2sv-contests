from collections import Counter


recipe = Counter(input())
for ingredient in ['B', 'S', 'C']:
    if ingredient not in recipe:
        recipe[ingredient] = 0

print(recipe)

nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())

rubles = int(input())

rubles += nb * pb if recipe['B'] else 0
rubles += nc * pc if recipe['C'] else 0
rubles += ns * ps if recipe['S'] else 0

needed = pb * recipe['B'] if recipe['B'] else 0
needed += ps * recipe['S'] if recipe['S'] else 0
needed += pc * recipe['C'] if recipe['C'] else 0

print(rubles // needed)