# Pause code
# 추후에 다시 풀어 볼 것

n = int(input())
p = sorted([list(map(int, input().split())) for _ in range(n)])

print(type(p))
psum = n * 100
for i in range(n - 1):
    if p[i][0] + 10 > p[i+1][0] and (p[i][1] + 10 > p[i+1][1] or p[i+1][1] + 10 > p[i][1]):
        if p[i][1] > p[i+1][1]:
            psum -= (p[i][0] + 10 - p[i+1][0]) *(p[i][1] + 10 - p[i+1][1])
        else:
            psum -= (p[i][0] + 10 - p[i+1][0]) *(p[i+1][1] + 10 - p[i][1])
print(psum)