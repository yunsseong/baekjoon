# Success code
# E S M 값을 받고 이 값까지 도달 하도록 1 1 1 부터 숫자를 올려가며
# 찾아가는 브루트포스 알고리즘을 사용하였다.
# 숫자를 올릴때마다 범위 사이에 있는지 확인하고 범위를 벗어난다면
# 1로 다시 초기화하는 과정을 거쳤다.

E, S, M = list(map(int, input().split()))

e, s, m = 1, 1, 1

cnt = 1
while E != e or S != s or M != m:
    if m+1 <= 19: m += 1
    else: m = 1
    
    if s+1 <= 28: s += 1
    else: s = 1
    
    if e+1 <= 15: e += 1
    else: e = 1

    cnt += 1
print(cnt)