# Success code
# 문제에서 입력 받은 수로 나누었을때 나머지와 몫이 같은 숫자를 구해야하는데
# 몫과 나머지가 1부터 시작해서 하나씩 더해가면서 조건에 맞을때까지 누적하여 답을 구하였다.
# 성립하는 조건은 입력 받은 수에 몫을 곱하고 나머지를 더한 수를 다시 몫으로 나누었을때
# 나머지가 나오는지 확인하면 된다.

n = int(input())

cnt = 1
res = 0
while cnt:
    tmp = n * cnt + cnt
    if tmp % n == cnt:
        res += tmp
        cnt += 1
    else:
        break
print(res)