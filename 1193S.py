# Success code
# 분수표를 다 만드는 방식이 아닌 어디에 위치한지 알아내서 그 줄만 연산하는 방식을 취하였다.
# 몇 번째 줄에 위치한지는 누적합으로 범위 사이에 있는지 판별하면 된다.누적합은 가우스 합을 사용하였다.
# 몇 번째 칸에 위치한지는 위치하기 전줄까지의 누적합을 입력 받은 숫자에 빼면 나온다.

import sys
n = int(sys.stdin.readline().rstrip())

def gauss_sum(n):
    return int((n+1) * n / 2)

def mix(a, b):
    return f'{a}/{b}'

appr = 0
loc = 0
if n != 1:
    for i in range(2, 10000000):
        if gauss_sum(i-1) < n <= gauss_sum(i):
            appr = i
            break
else:
    print('1/1')
    sys.exit()
    
loc = n - gauss_sum(appr - 1)

tmp = [j for j in range(1, appr + 1)]
if appr % 2 != 0:
    res = list(map(mix, tmp, tmp[::-1]))[::-1][loc-1]
else:
    res = list(map(mix, tmp, tmp[::-1]))[loc-1]

print(res)