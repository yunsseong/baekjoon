# Success code, 현재 랭킹에 있는 점수 리스트에 태수의 점수를
# append하고 비오름차순으로 정렬하고 태수의 점수가 나올때까지 리스트를
# 돌리면서 돌린 수만큼 카운트하는 것이 프로그램의 핵심이다.

import sys
n, t, p = list(map(int, input().split()))
if n != 0:
    s = list(map(int, input().split()))
else:
    print(1)
    sys.exit()
ns = s.copy()
ns.append(t)
ns.sort(reverse=True)
cnt = 0

if s[-1] == t and len(s) >= p:
    print(-1)
else:
    for sc in ns:
        cnt += 1
        if sc == t and p >= cnt:
            print(cnt)
            break
        elif p < cnt:
            print(-1)
            break

