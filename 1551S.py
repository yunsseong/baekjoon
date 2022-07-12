# Success code
# i+1번째 수열에서 i번째 수열을 빼는데 이를 원하는 횟수만큼 반복 해야해서 재귀 함수를 사용하였다.

n, k = list(map(int, input().split()))
a = list((map(int, input().split(","))))

def trans(cnt, sequence):
    if cnt != k:
        tmp = []
        for i in range(len(sequence)-1):
            tmp.append(sequence[i+1] - sequence[i])
        return trans(cnt + 1, tmp)
    else:
        return sequence

print(",".join(map(str, trans(0, a))))