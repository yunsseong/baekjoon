# Fail code
# 입력 받은 숫자가 전부 서로소인 경우
# 값을 배수로 해서는 겹치는 배수는 구할 수 없다.

from collections import Counter
nums = list(map(int, input().split()))
mul = []
n = 1

while n:
    mul.extend([i*n for i in nums])
    cnt = Counter(mul)
    if max(cnt.values()) >= 3:
        break
    n += 1

print(cnt.most_common(1)[0][0])