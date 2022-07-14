x, y = list(map(int, input().split()))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
def day_of_week(num):
    print(week[num % 7 -1])

tmp = 0
for i in range(x-1):
    tmp += days[i]
day_of_week(tmp + y)

