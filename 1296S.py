key = input()
n = int(input())

def cnt_love(name):
    dict_love = {'L':0, 'O': 0, 'V': 0, 'E': 0}
    for i in name:
        if i in ['L', 'O', 'V', 'E']:
            dict_love[i] += 1
    return dict_love

def sum_love(yeondo, team_name):
    list_love = []
    for a, b in zip(yeondo.values(), team_name.values()):
        list_love.append(a + b)
    return list_love

def trans(list_love):
    tmp = 1
    for i in range(len(list_love)):
        for j in range(i+1, len(list_love)):
            tmp = tmp * (list_love[i] + list_love[j])
    res = tmp % 100
    return res

yeondo_cnt = cnt_love(key)

name_tmp = []
res_tmp = []
for _ in range(n):
    name = input()
    name_tmp.append(name)

name_tmp.sort()

for name in name_tmp:
    name_cnt = cnt_love(name)
    name_cnt_sum = sum_love(yeondo_cnt, name_cnt)
    res_tmp.append(trans(name_cnt_sum))

print(name_tmp[res_tmp.index(max(res_tmp))])