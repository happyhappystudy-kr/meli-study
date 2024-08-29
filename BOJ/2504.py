input_str = input().strip()
stack = []

for ch in input_str:
    if ch in ["(", "["]:
        stack.append(ch)
    elif ch == ")":
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            print(0)
            exit(0)
    else:
        if stack and stack[-1] == "[":
            stack.pop()
        else:
            print(0)
            exit(0)

if stack:
    print(0)
    exit(0)

for ch in input_str:
    if ch == "(":
        stack.append((ch, 2))
    elif ch == "[":
        stack.append((ch, 3))
    else:
        last1, last2 = stack.pop()
        if last1 != None:
            stack.append((None, last2))
        else:
            temp = last2
            a, b = stack.pop()
            while a == None:
                temp += b
                a, b = stack.pop()
            stack.append((None, b*temp))

answer = 0
while stack:
    _, score = stack.pop()
    answer += score
print(answer)
