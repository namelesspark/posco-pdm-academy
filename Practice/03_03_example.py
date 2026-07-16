print("=== 실습 - len() 으로 길이 재기 ===")
effector = "strymon Timeline MX"  # 예상 결과 19
print(len(effector))


print("\n=== 실습 - in으로 포함 확인 ===")
msg = "설비 고장 발생"
print("설비" in msg and "고장" in msg)
print("정상" in msg)

print("\n=== 실습 - count()로 개수 세기 ===")
variable = "a,b,c,d"
print("문자열: " + variable)
print("콤마 개수: " + str(variable.count(",")))

print("\n=== 실습 - find()로 위치 찾기 ===")
variable = "Predictive Maintenance"
print("문자열: " + variable)
print("e 위치: " + str(variable.find("e")))
print("b 위치: " + str(variable.find("b")))


print("\n=== 실습 - startswith / endswith ===")
f_name = "sensor_log.csv"
print(f_name.startswith("sensor"))
print(f_name.endswith("csv"))

print("\n=== 실습 - '=='로 대소문자 구분 비교 ===")
status = "WARNING"
print(status == "WARNING")
print(status == "warning")
