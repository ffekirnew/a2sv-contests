def solve():
    string = input()

    ab_count = string.count("AB")
    ba_count = string.count("BA")

    if not ab_count or not ba_count:
        print("NO")
        return

    # if there are more than one, the answer is alweays yes
    if ab_count > 1 and ba_count > 1:
        print("YES")
        return
    
    # if they are 1 each, we need to know where they are appearing
    if ab_count == ba_count == 1:
        ab_index = string.index("AB")
        ba_index = string.index("BA")
        if abs(ab_index - ba_index) > 1:
            print("YES")
        else:
            print("NO")
        return
    
    if ab_count == 1 and ba_count == 2 or ab_count == 2 and ba_count == 1:
        print("NO")
        return

    print("YES")
    return
        

if __name__ == "__main__":
    solve()