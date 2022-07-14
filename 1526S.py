# Success code
# checker 함수를 통해 문제에서 요구하는 형태인지 확인하고 아니라면 값을 하나씩 줄여가면서 찾는 방식

n = int(input())
num_filter = ['0', '1', '2', '3', '5', '6', '8', '9']

def checker(num):
    tmp = str(num)
    for i in tmp:
        if i in num_filter:
            return True
    return False

while checker(n):
    n -= 1

print(n)
