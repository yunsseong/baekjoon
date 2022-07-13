# Success Code
# 직접 카운트 하는 방식을 보다 X를 기준으로 split하여 .의 갯수가 2 이상인 것을 카운트 했다.
# 이렇게 하면 ..X..인 경우도 처리 할 수 있다.

n = int(input())

std = []
for _ in range(n):
    std.append(input())

def trans(a_map):
    tmp = []
    for i in a_map:
        tmp.append(i.split('X'))
    return tmp

def x_split_join(a_map):
    tmp = []
    for j in a_map:
        tmp.append(''.join(j).split('X'))
    return tmp

hol_map = trans(std.copy())
var_map = x_split_join(list(map(list, zip(*std))))

def checker(xmap):
    cnt = 0
    for case in xmap:
        for item in case:
            if len(item) >= 2:
                cnt += 1
    return cnt

print(checker(hol_map), checker(var_map))