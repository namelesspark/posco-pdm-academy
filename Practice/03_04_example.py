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

print("\n=== strip() 실습 ===")
raw = "         정상         "
print(raw.strip())
print(raw.lstrip())
print(raw.rstrip())
raw = "     정      상       "
print(raw.strip())

print("\n=== 체이닝 실습 ===")
warning = "     Warning     "
warning = warning.lower().strip()
print("[" + warning + "]")


print("\n=== 쉼표 기준으로 나누기 ===")
abcd = "a,b,c,d"
abcd_split = abcd.split(",")
print(abcd_split)


print("\n=== 실습 5 - 리스트 합치기 ===")
date = ["2025", "01", "15"]
print("-".join(date))

# pyThon이라고 출력하기

print("\n=== pyThon 출력하기 ===")
python = "python"

print("방법 1")
print(python.index("t"))  # 2
print(python[0:2] + python[2].upper() + python[3:])

print("\n방법 2")
print(python.replace("t", "T"))

print("\n 방법 3")
print(python[0] + python[1] + python[2].upper() + python[3] + python[4] + python[5])
