# 자리배치
# 입장객 수, 좌석 열, 줄수
# 입장객 수가 열수로 나누어떨어지는 경우, 그렇지 않은 경우
customer = int(input("입장객 수 입력: "))
col = int(input("좌석 열 수 입력: "))

# 몫 = customer/ col
# 나머지 = customer % col
# print(몫)
# print(나머지)

if customer % col == 0:
   # row = customer // col
   row = int(customer / col)    # 여기 int 안 하면 정수로 안 나옴
else:
    # row = customer // col + 1
    row = int(customer / col) + 1
print("줄수:", row)

