# 실습 01 - 사칙연산 계산기
def calculator(a, b):
    return a + b, a - b, a * b, a / b, a // b, a % b


print(calculator(10, 4))


# 실습 02 - 평균과 도형 계산 / 응용
width = 80
height = 91
depth = 100
print("평균:", (width + height + depth) / 3)

print("width와 height를 길이로 가지는 사각형의 넓이:", width * height)

print("부피:", width * height * depth)
