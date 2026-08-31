# 산술 연산자
# + - * /
# // % **

print(3 + 5)  # 8
print(10 - 4)  # 6
print(4 * 5)  # 20
print(20 / 4)  # 5
print(7 // 2)  # 2 7을 나누었을 때의 몫
print(7 % 3)  # 1: 7을 나누었을 때의 나머지
print(8**2)  # 64

# ====================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱)    >    *(곱), /(나누기), //(몫), %(나머지)    >    +(더하기), -(빼기)


print("\n===== 연산 우선순위와 우선순위 지정=====")
print(2**2 % 3)

print("\n")
result = 3 * 5
print(result)  # 15
# +=: 현재 변수에 오른쪽 값을 재할당하는 연산자
# -=
# *=
# /=
# //= ->
# %=  -> 이거 두개도 됨

# 많이 있다

result %= 3
print(result)

result += 10
print(result)
result -= 5
print(result)
result *= 8
print(result)
result /= 3
print(result)

# ==========
print("\n===== 문자열 연산 =====")
print("안녕" + "하세요")  # 안녕하세요

# 만약 안녕과 하세요 사이에 공백을 1개 넣고 싶다면
# 방법 1: , 사용
print("안녕", "하세요")

# 방법 2: 안녕 뒤에 공백 추가
print("안녕 " + "하세요")

# 방볍 3: 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")


# 문자열 곱하기
print("안녕" * 5)


# ==========

print("\n=== 비교 연산자 ===")
# <(미만), >(초과), <=(이하), >=(이상)

print(7 < 16)  # True
print(7 > 16)  # False
print(7 <= 16)  # True
print(8 >= 8)  # True
print(7 != 16)  # True
print(7 == 16)  # False

# 비교 연산자는 문자열 비교도 가능하다
print("=== 비교 연산자는 문자열 비교도 가능하다 ===")
print("hello" == "hello")  # True
print("정상" == "정상")  # True


# 문자열 비교할 때 주의사항
# 1. 대소문자 구분
print("Hello" == "hello")

# 2. 공백 구분
print("정상" == "정상 ")

# 3. not 연산자로, 두 개가 다른게 "맞기" 때문에 True
print("hello" != "hello ")

# 응용
hello = "hi"
print(hello == "hi")  # True
# 위 비교에서 hello는 따옴표로 감싸지지 않아서 "변수"로 취급
# 만약 hello를 "hello"와 같이 따옴표로 감싸면
# string으로 인식해서 변수 취급을 하지 않음
# 따옴표로 감싸면 "hello"와 "hi"를 비교하는 것과 마찬가지다.

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2)  # False
# print(num1 >= "num2")  # False? No TypeError 발생

print("문자열 할당된 변수를 다른 변수에 할당 후 출력해보기")
hi = "안녕"
hello = hi
print(hello == "안녕")

# =======================================================
# 논리 연산자
# and, or, not, nand, nor, xor
# and: 곱, 둘 다 참
# or: 합, 하나만 참
# not: 부정(반대)
# nand: and의 부정
# nor: or의 부정
# xor: 배타적 or, 다르면 참
print("\n===== 논리 연산자 =====")
print(5 == 5 or 7 == 7)  # True or True = True
print(5 == 5 and 7 == 7)  # True and True = True
print(5 == 5 or 7 == 5)  # True or False = True
print(5 == 5 and 7 == 5)  # True and False = False

# or는 첫 번째 조건이 True라면 뒤에 올 조건은 확인 안함
print("or는 첫 번째 조건이 True라면 뒤에 올 조건은 확인 안함")
print(5 == 5 or 7 != 7)  # 결과는 True

# not 연산자: 부정 연산자(!) 반대로 뒤집는다.

print("not 연산자: 부정 연산자(!) 반대로 뒤집는다.")
print(not 5 == 5)
# 5 == 5를 연산하여 True를 반환
# not True로 동작해서 True를 뒤집어 False를 반환
# 반환받은 False라는 값을 print가 터미널로 출력
