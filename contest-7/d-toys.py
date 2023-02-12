from collections import Counter


if __name__ == "__main__":
    prices_nums, toys_needed = map( int, input().split() )

    prices = list( map( int, input().split() ) )
    prices.sort()

    toy_names = [ input() for toy in range(toys_needed) ]
    toy_freqs = Counter(toy_names)

    toys = [ [ key, value ] for key, value in toy_freqs.items() ]
    toys.sort( key=lambda x: x[1], reverse=True )

    minimum = 0
    price_idx = 0
    for toy in toys:
        minimum += prices[ price_idx ] * toy[1]
        price_idx += 1

    maximum = 0
    price_idx = prices_nums - 1
    for toy in toys:
        maximum += prices[ price_idx ] * toy[1]
        price_idx -= 1
    
    print(minimum, maximum)
