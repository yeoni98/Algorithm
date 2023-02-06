n = int(input())
l = []

if n%5 == 0:
    l.append(n/5)
elif n!=6 and n%5 == 1:
    l.extend([2, (n-6)/5])
elif n!=7 and n%5 == 2:
    l.extend([4, (n-12)/5])
elif n%5 == 3:
    l.extend([1, (n-3)/5])
elif n!=4 and n%5 == 4:
    l.extend([3, (n-9)/5])
elif n%3 == 0:
    l.append(n/3)
else:
    l.append(-1)
print(int(sum(l)))
