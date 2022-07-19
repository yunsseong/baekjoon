# Success code
# 입력 받은 문자열을 for문에 넣어 X를 카운트하고 
# 만약 X가 아닌 다른 문자열이 나온다면
# 그전에 카운트를 기준으로 카운트가 4 이상이면 AAAA를
# 카운트가 2일때는 BB를 res변수에 카운트 변수가 0이 될때까지 더하였다.
# 만약 카운트 변수가 위의 범위에서 벗어난다면 -1을 출력하고 중단한다.

import sys
board = input()
board = board + 'E'
cnt = 0
res = ''

for x in board:
    if x == 'X':
        cnt += 1
    else:
        while cnt > 0:
            if cnt >= 4:
                res += 'AAAA'
                cnt -= 4
            elif cnt == 2:
                res += 'BB'
                cnt -= 2
            else:
                print(-1)
                sys.exit()
        if x == 'E':
            break
        else:
            res += '.'
print(res)

            