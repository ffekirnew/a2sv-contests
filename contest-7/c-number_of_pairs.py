if __name__ == "__main__":

    answer = 0

    num_b = int( input() )
    b = list( map( int, input().split() ) )
    num_g = int( input() )
    g = list( map( int, input().split() ) )

    b.sort()
    g.sort()

    p1, p2 = 0, 0

    while p1 < num_b and p2 < num_g:
        if abs( b[ p1 ] - g[ p2 ] ) <= 1:
            answer += 1
            p1 += 1
            p2 += 1

        elif b[ p1 ] - g[ p2 ] > 1:
            p2 += 1

        elif g[ p2 ] - b[ p1 ] > 1:
            p1 += 1
        
    print(answer)