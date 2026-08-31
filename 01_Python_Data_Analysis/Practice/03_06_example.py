print("\n=== 실습 1 - f-string으로 변수 끼워 출력하기 ===")
name = "PUMP-A"
temp = 87
print(f"설비: {name}, 온도: {temp}")


print("\n=== 실습 2 - f-string 안에서 계산하기 ===")
num1, num2, num3 = 72, 84, 120
print(f"평균: {(num1 + num2 + num3) / 3}")

print("\n=== 실습 3 - 소수점 자리수 지정하기 ===")
val = 87.456
print(f"{val:.2f}")


print("\n=== 실습 4 - 센서 로그 한 줄 정리 리포트 만들기 ===")
sensor_log = " 5 , sensor_2 , WARNING , 0.78912 "
sensor_log_c = sensor_log.strip().lower().split(",")
print(f"[센서 {sensor_log_c[1]} 상태 {sensor_log_c[2]} 측정값 {sensor_log_c[3]}]")
