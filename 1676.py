# Success, 입력 받은 숫자의 팩토리얼을 구한후
# 문자열화하고 리버스한다음 for 문에 넣는다.
# 처음으로 0이 아닌 숫자가 나올때까지 카운트 해주면 된다.

n = int(input())

fac = 1
while n:
    fac = fac * n
    n -= 1

cnt = 0

for i in str(fac)[::-1]:
    if i != '0':
        break
    else:
        cnt += 1
print(cnt)
