# 트레이스백으로 에러 읽기

# ValueError: 글자를 숫자로 변환 요구 - 당연히 실패
# temp = int("스믈")

# Traceback (most recent call last):
#   File "/Users/nedpark/Desktop/handler1.py", line 4, in <module>
#     tmep = int ("스믈")
#            ~~~~^^^^^^^^
# ValueError: invalid literal for int() with base 10: '스믈'

# 정상화
temp = int("20")
print(temp)

print("=" * 20)

# ZeroDivisionError : 숫자는 0으로 나뉠 수 없어요
# result = 10 / 0

# Traceback (most recent call last):
#   File "/Users/nedpark/Desktop/handler1.py", line 19, in <module>
#     result = 10 / 0
#              ~~~^~~
# ZeroDivisionError: division by zero

# 정상화
result = 10 / 3
print(result)

print("=" * 20)

# NameError : 그런 이름도 있었어요?라는 뜻의 에러
# hello()

# Traceback (most recent call last):
#   File "/Users/nedpark/Desktop/handler1.py", line 32, in <module>
#     hello()
#     ^^^^^
# NameError: name 'hello' is not defined. Did you mean: 'help'?

# 정상화
print("Hello")


temp = -1

try:
    temp = int("스믈")
except:
    print("해봤는데 안되네요")
    temp = 0  # 문제가 있어도 앞으로 잘 진행되도록 대안/추가 처리 필요

print(temp)


# 09_01_예외처리_기초
# 실습 2

origin = input("온도 : ")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except ValueError:
    # ValueError인 상황이었다면 여기로 예외처리
    print("숫자 아니면 왜 저를 부르셨어요? 0으로 생각할께요")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")

# 09_01_예외처리_기초
# 실습 2

origin = input("온도 : ")

print(f"입력한 온도는 {origin}")

temp = 0

try:
    temp = int(origin)
except ValueError:
    # ValueError인 상황이었다면 여기로 예외처리
    print("숫자 아니면 왜 저를 부르셨어요? 0으로 생각할께요")
except TypeError:
    # TypeError인 상황이었다면 여기로 예외처리
    print("타입 문제는 전지구적 문제입니다.")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")


# 09_02
# else와 finally 코드
text = "text"
try:
    temp = float(text)
finally:
    print("종료")  # 성공 / 실패 뭐든지 무조건 실행
