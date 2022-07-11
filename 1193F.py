# fail code
# 이유 : 분수를 다 담고 있는 리스트를 만들고 시작하려고 했지만
# 입력 범위가 1부터 10,000,000까지여서 1000까지만 만들어도 시간이 너무 오래 걸림
# 해결 방안 : 입력값이 대충 표에 어디 있는지 가늠한 다음에 그 위치면 연산해서 출력하면 될듯하다.

frac = []
def mix(a, b):
    return f'{a}/{b}'
for i in range(1, 1000):
    tmp = [j for j in range(1, i + 1)]
    if i % 2 != 0:
        frac.extend(list(map(mix, tmp, tmp[::-1]))[::-1])
    else:
        frac.extend(list(map(mix, tmp, tmp[::-1])))
print(frac)

n = int(input())
print(frac[n])

#