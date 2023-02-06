import sys
import math


n = int(sys.stdin.readline())
for i in range(n):
    word = input()
    num = len(word)

    if word == word[::-1]:
            print('0')




    else:
        start = list(word)
        end = list(word)

        for i in range(math.ceil(int(len(word)/2))):

            if word[i] != word[-(i+1)]:
                start.pop(i)
                end.pop(-(i+1))


                if start == start[::-1]:
                    print('1')
                    break
                if end == end[::-1]:
                    print('1')
                    break

                print('2')
                break