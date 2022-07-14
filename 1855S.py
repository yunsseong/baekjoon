# Success code
# 입력 받은 문자열을 전체길이에서 열 갯수만큼 나눈 수 단위로 나누어
# 홀수 번째는 정순으로 짝수 번째는 역순으로 하여 새로운 문자열을 만든다.
# 그후 열 갯수 만큼의 간격으로 문자열을 가져와서 더하여 원본 문자열을 만든다.

n = int(input())
str_list = list(input())
unit = len(str_list)//n

tmp = ''
dec = ''
for s in range(unit):
    for i in range(n):
        if s % 2 == 0:
            tmp += str_list.pop(0)
        else:
            tmp = str_list.pop(0) + tmp
    dec += tmp
    tmp = ''
res = ''

for i in range(n):
    for j in range(unit):
        res += dec[i + j * n]
    
print(res)
