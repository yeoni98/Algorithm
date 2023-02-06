n = int(input())
number = list(map(int, input().split()))

lst = []

for i in number:
    for j in range(2, i+1):
        if j == i:
            lst.append(i)
        if i % j == 0:
            break


print(len(lst))