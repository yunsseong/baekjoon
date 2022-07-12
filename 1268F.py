# Fail code
# 이유 : 같은 학년일때 2반 이상 같은 반을 나온 학생이 2명 이상일 경우에 대해 처리할 로직이 없어서 실패

from collections import Counter 

n = int(input())
stu_list = []

for _ in range(n):
    stu_list.append(input().split())

grade_list = []
for i in range(5):
    tmp = []
    for j in range(len(stu_list)):
        tmp.extend(stu_list[j][i])
    grade_list.append(tmp)
    tmp = []

overlab_max_num = []

for j in grade_list:
    if list(dict(Counter(j)).values()) == [1 for i in range(len(list(dict(Counter(j)).values())))]:
        overlab_max_num.append(" ")
    else:
        overlab_max_num.append(max(dict(Counter(j)), key = dict(Counter(j)).get))



overlab_cnt = [0 for i in range(len(stu_list))]

for x, stu in enumerate(stu_list):
    for m in range(5):
        if stu[m] == overlab_max_num[m]:
            overlab_cnt[x] += 1

order_list = [i for i in range(len(stu_list))]
overlab_cnt_dict = dict(zip(order_list, overlab_cnt))

res = sorted(overlab_cnt_dict.items(), key = lambda x : (-x[1], x[0]))[0][0] + 1

print(res)




