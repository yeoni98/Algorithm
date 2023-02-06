import sys


nums = list(map(int,sys.stdin.readline().rstrip()))
result = []
while nums:
    result.append(max(nums))
    nums.remove(max(nums))

print(*result, sep='')