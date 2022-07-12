# Success code
# 크로스 체크 할 수 있게 학생들 숫자를 기준으로 표를 만들고 서로 비교하는 알고리즘 사용

n = int(input())
stu_list = []
for _ in range(n):
    stu_list.append(input().split())

compare = [[0 for i in range(n)] for i in range(n)]
for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if stu_list[j][i] == stu_list[k][i]:
                compare[j][k] = 1
                compare[k][j] = 1

cnt = []
for s in compare:
    cnt.append(s.count(1))

print(cnt.index(max(cnt))+1)
