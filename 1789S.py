# Success code
# 수를 누적하여 입력 받은 수를 넘어가기 직전까지 카운트 하면
# 이 값이 서로 다른 N개의 자연수 합에서 N이 최대가 될때이다.
# 입력 받은 수를 넘어가기 직전의 자연수가 n이라면 그 다음 자연수
# n + 1을 더한 후 넘어가는 것 만큼 이전에 누적한 것에서 빼면 되기 때문에
# N의 갯수가 한번 더하고 빼지므로 입력 받은 수를 넘어가기 직전까지의 갯수만 구하면 된다.

n = int(input())

def gauss(num):
    return (1 + num) * (num) // 2
    
cnt = 1
while gauss(cnt) <= n:
    cnt += 1
  
print(cnt-1 if cnt != 1 else 1)