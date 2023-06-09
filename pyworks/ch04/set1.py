# 집합 - set(), {}를 사용, 순서가 없다, 중복 불허

s = {2, 4, 6 ,8, 8}

# 요소 추가
s.add(10)

# 요소 삭제
s.remove(4)

print(2 in s) #T/F로 출력됨
print(3 in s)

# 전체 삭제
s.clear()

# 전체 조회
for i in s:
    print(i)

print(s)  #출력 시 순서 상관없이 나옴 막 나옴 8 한번 나옴


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# 교집합(A&B), 합집합(A|B), 차집합(A-B)
print(A & B)
print(A | B)
print(A - B)

# 자료 중복 제거
a = [1, 1, 1, 2, 2, 3]
s = set(a)
print(s)
# 리스트로 변환
print(list(s))

say = set('Hello')
print(say) #{'e', 'H', 'l', 'o'} - 순서없고, 중복없음

# 1에서 10까지의 자연수를 저장
C = { x for x in range(1, 11)}
print(C)

# 1에서 20까지의 자연수 중에서 3의 배수 저장
D = { x for x in range(1, 21) if x % 3 == 0}
print(D)