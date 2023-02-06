import sys

box = []
length = []

for i in range(5):
    word = input()
    box.append(word)
    length.append(len(word))

result = []

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result.append(box[j][i])

print(''.join(result))
