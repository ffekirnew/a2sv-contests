from collections import Counter
def main():
    stones = input().split()
    stones = Counter(stones)
    if (len(stones) >= 5):
        print("YES")
    else:
        print("NO")
 
if __name__ == "__main__":
    main()