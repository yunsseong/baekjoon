# 다솜이가 매수해야할 사람의 최솟값을 구하는 방법은 다음과 같다.
# 다솜이를 제외한 사람들을 모아 놓은 리스트를 만들고
# 거기서 득표수가 제일 많은 사람 A를 뽑고 다솜이 표보다 작아질때까지
# A의 표를 한표씩 줄여나가고 다솜이 표에 한표씩 늘려나가는 것이다.
# 만약 A의 표가 다솜이 보다 작으나 다솜이 보다 표가 많은 사람이 존재 할 수 있으므로
# 동일한 과정을 반복한다.

import sys
n = int(input())

if n == 1:
    input()
    print(0)
    sys.exit()
num = []
for _ in range(n):
    num.append(int(input()))
d, p = num[0], num[1:]

cnt = 0
while d <= max(p):
    p[p.index(max(p))] -= 1
    d += 1
    cnt += 1

print(cnt)

