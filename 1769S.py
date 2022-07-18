# Success code
# 이 문제는 받은 문자열을 리스트와 시켜 자리별로 분해 시킨 다음
# map 함수를 통해 각각의 요소를 인트화하고 다시 리스트에 넣는다.
# 그 리스트를 sum 함수를 통해 각각의 요소를 다 더하고 str 함수를 통해 문자화 한 후
# 다시 리스트에 넣어서 자리수 별로 분해하고 리스트의 크기를 확인하는 것이 주요 기능이다.
# 리스트의 길이가 2 이상일때 동안 수행하면 원하는 결과 값을 얻을 수 있다.

n = list(str(sum(list(map(int, list(input()))))))
length = len(n)

if length == 1:
    cnt = 0
else:
    cnt = 1

while length >= 2:
    n = list(str(sum(list(map(int, n)))))
    length = len(n)
    cnt += 1

print(cnt)
if sum(list(map(int, n))) % 3 == 0:
    print('YES')
else:
    print('NO')



