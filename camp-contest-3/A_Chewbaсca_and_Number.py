num = input()
 
answer = []
 
for i, n in enumerate(num):
    if i == 0 and int(n) == 9:
        answer.append("9")
    elif 5 <= int(n):
        answer.append(str(9 - int(n)))
    else:
        answer.append(n)
 
print("".join(answer))