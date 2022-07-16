# Success code
# 입력 받은 숫자가 0이 아닐때까지 입력 받은 수 만큼 for 문을 돈다.
# for 문 사이에는 단어를 입력 받는다.
# 이때 단어를 소문자한 것을 키로 하고 그 값으로 원본 문자를 갖는 딕셔너리를 만든다.
# 단어를 다 입력 받은 다음 딕셔너리를 정렬하고 첫번째 아이템을 가져와 값을 출력한다.


while 1:
    n = int(input())
    if n == 0: break
    words = {}
    for _ in range(n):
        tmp = input()
        words[tmp.lower()] = tmp
    print(sorted(words.items())[0][1])

