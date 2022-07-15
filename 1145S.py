# Success code
# 5개 중 3개를 조합을 써서 뽑아서 최소 공배수를 구하고
# 구한 최소 공배수 중에서 가장 작은 것을 출력하도록 하였다.
# 최소 공배수는 유클리드 호제법을 사용하여 구현하였다.

from itertools import combinations

nums = list(map(int, input().split()))

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    result = (x * y)//gcd(x, y)
    return result

def get_3_lcm(x, y, z):
    return lcm(lcm(x, y), z)

def combi(nums):
    res = 1000000
    combi_list = list(combinations(nums, 3))
    for a, b, c in combi_list:
        tmp = get_3_lcm(a, b, c)
        if tmp < res:
            res = tmp
    return res

print(combi(nums))

