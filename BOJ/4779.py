solutions = ["-"]
for i in range(1, 13):
    solutions.append(solutions[i-1] + " "*(3**(i-1))+solutions[i-1])
while True:
    try:
        n = int(input())
        print(solutions[n])
    except: break

##recursive
def sol(n):
    if n == 0:
        return "-"
    else:
        return sol(n-1)+ " "*(3**(n-1))+sol(n-1)
while True:
    try:
        n = int(input())
        print(sol(n))
    except: break
