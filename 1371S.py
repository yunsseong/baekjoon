# Success code
# 입력 값들의 갯수가 정해지지 않았기 때문에 End Of File Error가 발생할때까지 값을 받는다.
# 그리고 Counter 함수를 통해서 입력값의 알파벳 빈도수를 구하고 most_common 함수를 통해 최빈값을 구한다.
# 문제에서 최빈값이 같을 경우 알파벳순으로 연이어 출력하라고 했기 때문에 최빈값이 같은 값을 찾아 연결해서 출력한다.

from collections import Counter

lines = ""
while True:
    try:
        line = input()
        for s in line:
            if s.isalpha():
                lines += s
    except EOFError:
        break

a = Counter(lines)
order = a.most_common()
most_num = a.most_common(1)[0][1]
most = []

for item in order:
    if item[1] == most_num:
        most.append(item)

res = ""
most.sort()
for item in most:
    res += item[0]

print(res)
