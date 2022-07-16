# Success
# 리스트 컴프리션을 통해서 문제에서 필요한 형태의 리스트를 만들고
# 리스트 슬라이싱을 통해서 구간을 특정한 다음 sum 함수를 통해 구간의 합을 구하였다.

a,b =list(map(int,input().split()))
print(sum([x for y in [[i for _ in range(1,i+1)] for i in range(1,1001)] for x in y][a-1:b]))
