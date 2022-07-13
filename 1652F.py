# Fail code
# ..X.. 일때를 고려하지 않았음

n = int(input())

room = []
for _ in range(n):
    room.append(input())

hor = 0
ver = 0

def checker(room):
    cnt = 0
    flg = 0
    for line in room:
        for i in range(n-1):
            if line[i] == '.' and line[i+1] == '.':
                flg = 1
                break
        if flg:
            cnt += 1
            flg = 0          
        
    return cnt

hor += checker(room)
s_room = list(map(list, zip(*room)))
ver += checker(s_room)

print(hor, ver)