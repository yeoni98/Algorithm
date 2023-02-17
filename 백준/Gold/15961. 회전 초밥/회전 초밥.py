import sys
from collections import defaultdict

n, d, k, c = map(int,sys.stdin.readline().split())
sushi = []



for i in range(n):
    sushi.append(int(sys.stdin.readline()))
sushi += sushi[:k-1] # sushi*2라고 했는데 그것보다 sushi 마지막에서 + k-1개만큼만 더 있으면 되니까

left, right, cnt = 0, 0, 0
eat = defaultdict(int)
eat[c] += 1

def maximum(sushi):
    global cnt, right, left
#global 선언을 꼭 해줘야됨 변수 cnt, right,left가 maximum함수 안에 존재하지 않으니 a를 전역네임스페이스에서 함수안으로 땡겨와 사용할 수 있게 한 것이다.
#따라서 global선언 없이 함수 내에서 전역변수를 사용할 경우, print(cnt) , if cnt == 1: 과 같이 조회하는 기능만 가능하다.
#cnt값을 변경하는 것과 같이 "할당"(예를 들어 cnt = max(cnt, len(eat))을 해주려면 global선언이 필수적이다.
#참고:https://velog.io/@hongsikcho/%ED%8C%8C%EC%9D%B4%EC%8D%AC-referenced-before-assignment%EC%97%90%EB%9F%AC-%EC%9D%B4%EC%9C%A0%EC%99%80-%ED%95%B4%EA%B2%B0

    for right in range(len(sushi)):
        eat[sushi[right]] +=1

        if right >= k-1:
            cnt = max(cnt, len(eat))
            eat[sushi[left]] -= 1
            if eat[sushi[left]] == 0:
                del eat[sushi[left]]
            left +=1
    print(cnt)




maximum(sushi)
