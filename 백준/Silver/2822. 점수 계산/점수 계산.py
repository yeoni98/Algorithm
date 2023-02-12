import sys
score = []
ans = []
final_score = []

for i in range(8):
    score.append(int(sys.stdin.readline()))
    
#오름차순으로 정렬
num = sorted(score)
#4번째 값을 min으로 설정 (예제 1 기준으로 33)
min = num[3]
#33 보다 큰 값이 온다면 순서(i + 1)를 ans에 append, final_score에 점수 append
for i in range(8):
    if score[i] >= min:
        ans.append(i+1)
        final_score.append(score[i])


print(sum(final_score))
print(*ans)