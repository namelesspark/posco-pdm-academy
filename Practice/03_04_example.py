print("=== 실습 1 - 대문자로 바꾸기 ===")
ready = "ready"
ready = ready.upper()
print(ready)

print("=== 실습 2 -  소문자로 바꾸기 ===")
warning = "WARNING"
warning = warning.upper()
print(warning)

print("=== 실습 4 대소문자 무시하고 비교하기 ===")
str1 = "fault"
str2 = "FAULT"

print(str1 == str2)


print("=== 대문자인지 소문자인지 검사하기 ===")
u_case = "ABC"
l_case = "abc"
cap_case = "Abc"

print(u_case.isupper())
print(l_case.islower())
print(cap_case.isupper())

print("=== 실습 6 - 파일명 규칙 한 번에 점검하기 ===")
frame = "Sensor_LOG.CSV"
frame = frame.lower()

print(frame.startswith("sensor"))
print(frame.endswith("csv"))
