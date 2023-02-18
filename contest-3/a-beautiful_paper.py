def main():
    n = int(input())
    answer = []
    for i in range(n):
        rect_1 = list(map(int, input().split()))
        rect_2 = list(map(int, input().split()))

        if rect_1[0] == rect_2[0] and rect_1[1] + rect_2[1] == rect_1[0]:
            answer.append("YES")
        elif rect_1[0] == rect_2[1] and rect_1[1] + rect_2[0] == rect_1[0]:
            answer.append("YES")
        elif rect_1[1] == rect_2[0] and rect_1[0] + rect_2[1] == rect_1[1]:
            answer.append("YES")
        elif rect_1[1] == rect_2[1] and rect_1[0] + rect_2[0] == rect_1[1]:
            answer.append("YES")
        else:
            answer.append("NO")
            
                
    for ans in answer:
        print(ans)
    




if __name__ == "__main__":
    main()