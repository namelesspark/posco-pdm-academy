# + : 더하기
# - : 빼기
# * : 곱하기
# / : 나누기
# // : 몫
# % : 나머지

print(7 + 14)
print(7 - 14)
print(7 * 14)
print(7 / 14)
print(7 // 14)
print(7 % 14)
print(75 + 80 / 4)
print((75 + 80) / 4)  # 계산 순서 지정할 수 있다.

# 실습 - 계산 출력
Temperature_1st = 75
Temperature_2nd = 80

print("두", "측정값의", "합" + ":", Temperature_1st + Temperature_2nd)
print("온도", "변화량" + ":", abs(Temperature_1st - Temperature_2nd))
print("평균", "온도" + ":", (Temperature_1st + Temperature_2nd) / 2)


# =============================================

# 주석이란
# 샾 뒤에 적은 내용은 코드로 인식되지 않음.

# 실습 - 이해가 잘 안됐던 부분에 대하여 주석 달아보기
temperature = 75
vibration = 2.3

print("== " + "1번 " + "설비 " + "측정값 " + "==")
print(
    "온도(℃): " + str(temperature)
)  # temperature, vibration은 숫자형이므로, + 연산자를 사용하려면 따옴표를 붙이거나, str() 클래스 호출 후 형변환이 필요함.
print("진동(mm/s): " + str(vibration))
print("더하기 " + "연산자를 " + "사용하면?")
