count = 3
age = 20
height = 173

# 0rhk dmatneh wjdtndp vhgkaehla
temp = -30

# ==============================

# float - 실수
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수여도 무조건 float

tired = 99.99999
height = 17.2
emoji = "💯👀👾"
empty = ""  # 따옴표만 있어도 string

fake_num1 = "12345"
fake_num2 = "5.0"

# 따옴표가 "와 '' 둘 다 사용할 수 있는 이유는, 문자열 안에 따옴표가 필요한 경우가 있기 때문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 갖춰 가장 바깥에 감싸주기
illit = "It's me"

# ==============================

# bool 자료형
# True, False 밖에 없음
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
no = False

print(100 < 5)
print(100 > 5)


print("==== Type ====")

type(5)

print(type(5))
print(type("센서 A"))
print(type(True))

print(type(3 > 2))

# 산술 연산 -> bool 연산 -> type 확인

print(3, type(3))

num = 123
fake_num = "123"

# type()을 사용해서 출력된 결과물의 type을 확인할 수 있는 방법
print(num, ">>>", type(num))
print(fake_num, ">>>", type(fake_num))
