import sys
n = int(input())
files_lst =[]
files_dict = {}
for i in range(n):
    file = input()
    files = file.split('.')
    files_lst.append(files[-1])
for i in files_lst:
    if i in files_dict:
        files_dict[i] += 1
    else:
        files_dict[i] = 1

sorted_ = dict(sorted(files_dict.items()))
for key, value in sorted_.items():
    print(key, value)
