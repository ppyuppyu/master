# 수학 모듈 - math
# 절대값, 올림, 내림, 제곱근, 원주율
import math

# math의 속성
print(math.pi) # 원주율
print(math.ceil(2.54)) # 정수로 올림
print(math.floor(4.923)) # 정수로 내림(버림)
print(math.sqrt(25)) # 제곱근


# 내장 함수
print(round(11.78))
# 절대값
print(abs(-10))

# 1번 알고리즘
"""
# 절대값을 함수로 정의해보자

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

print(my_abs(-5))       # -5 -> -(-5), 5 -> 5
"""

# 2번 알고리즘

def my_abs2(x):
    y = x * x
    return math.sqrt(y)

# 제곱수(양수로 됨) -> 제곱근(실수로 표기)


print(my_abs2(-5))