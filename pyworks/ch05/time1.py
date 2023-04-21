# 시간 - time 모듈
import time

# 1970. 1. 1 자정 이후 지금까지 시간을 초로 환산
print(time.time())

# round() - 반올림 (정수로 반올림)
year = round(time.time()/(365*24*60*60))
day = round(time.time()/(24*60*60))
print(year)
print(day)

# 시간 정보 - 연도, 월, 일, 시, 분, 초
print(time.localtime())
print(time.ctime())

# 시간 측정
# 종료 시간(time.time()) - 시작 시간(time.time())
# time.sleep(1) - 1초 대기
# 1부터 10000까지 출력하는데 걸리는 시간
start = time.time()

for i in range(1, 10001):
    print(i)

end = time.time()
print(end - start)
