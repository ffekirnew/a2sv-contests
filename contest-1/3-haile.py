def main():
    n = int(input())
    information = []
    for i in range(n):
        information.append(input().replace("#", " "))
    for info in information:
        print(info)
 
if __name__ == "__main__":
    main()