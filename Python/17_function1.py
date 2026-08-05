print("안녕하세요")

name = "NED"
first_name = "Ned"
last_name = "Park"

print(first_name)
print(last_name)


def say_hello():
    print("안녕하세요")


say_hello()
say_hello()
say_hello()

# my_number = 123


# def show_number():
#     print(f"함수 시작: {my_number}")
#     my_number = 44
#     print(f"함수 시작: {my_number}")

#     print(my_number)


# my_number = 24
# show_number()

# my_number라는 변수를 언급하는 순간, 그런게 없다고 뜬다.
# show_number 안의 my_number와 바깥 my_number는 별개의 존재이다.

# 함수 안의 my_number 데이터가 영향을 끼치는 범위를 전문 용어로 "스코프"라 한다.

# 실습 1:


def show_counter():
    # count = count + 1 # 기존 count라는 존재는 모른다고 error
    count = 0
    print(count)


show_counter()
show_counter()
show_counter()


# 각 함수의 이름은 이름에 걸맞는 역할만 해줘야 한다


def show_student():
    print("학생1: 짱구")
    print("학생1: 철수")
    print("학생1: 훈이")
    print("선생님: 채송화")


show_student()
# 잘못 만든 함수가 되는거임

# [상식] 사이드이펙트 걸렸다 라는 말이 있다
# 특정 부분의 코드가 문제 없지만
# 다른 부분과 예쌍치 못한 영향을 주고 받는다면?

# 코드 중복과 함수화


print("-" * 100)


# 함수의 호출 결과 예측하기
def say_hi():
    print("안녕하세요")


say_hi()
say_hi()
