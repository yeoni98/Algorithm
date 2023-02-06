a, b, v = map(int, input().split())
n = (v-b)/(a-b)

if (v-b)%(a-b) == 0:
    print(int(n))
else:
    print(int(n)+1)