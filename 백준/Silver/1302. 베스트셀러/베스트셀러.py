import sys

n = int(sys.stdin.readline())

books = {}

for i in range(n):
    book = sys.stdin.readline().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
most_sold = sorted(books.items(), key = lambda item:item[1], reverse = True)
num = most_sold[0][1]

ans = []

for key, value in most_sold:
    if value == num:
        ans.append(key)
    else:
        break
print(sorted(ans)[0])