# Pause code

n, m = list(map(int, input().split()))
c_map = []
for _ in range(n):
    c_map.append(input())

tmp = []
for i in range(n-8):
    for j in range(m-8):
        for k in range(i+8):
            tmp.append(c_map[k][j:j+8])

print(tmp)
for x,i in enumerate(tmp):
    if (x+1) % 8 == 0:
        print(i)
        print('==========')
    else:
        print(i)
