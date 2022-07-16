# Success code
# 1월 1일을 기준으로 입력 받은 날짜가 얼마나 지났는지 계산하고
# 이를 7로 나눈 나머지를 구하면 요일에 따라 숫자가 대응 된다.
# 리스트의 인덱싱을 사용하여 요일을 바로 구할 수 있도록 구현하였다.
x, y = list(map(int, input().split()))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
def day_of_week(num):
    print(week[num % 7 -1])

tmp = 0
for i in range(x-1):
    tmp += days[i]
day_of_week(tmp + y)

