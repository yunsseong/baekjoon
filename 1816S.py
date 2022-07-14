# Success code
# 에라토스테네스의 체를 통해 1000000 사이 소수 리스트를 구한다.
# 입력 받은 숫자를 소수 리스트로 나누어서 만약 나누어 떨어진다면 'NO'를
# 나누어 떨어지지 않는다면 'YES'를 출력하였다.

def prime_list(n):
    sieve = [1] * n
    m = int(n**0.5) 
    for i in range(2, m + 1):
        if sieve[i] == 1:
            for j in range(i+i, n, i):
                sieve[j] = 0
    return [i for i in range(2, n) if sieve[i] == 1]

prime = prime_list(1000000)

def checker(num):
    for i in prime:
        if num % i == 0:
            return 'NO'
    return 'YES'

n = int(input())
for _ in range(n):
     print(checker(int(input())))
