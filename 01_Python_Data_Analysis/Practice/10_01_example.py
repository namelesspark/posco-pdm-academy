import random
import numpy as np

print("=" * 50)
print("=== 실습 1 - 센서값 배열 만들기 ===")
print("=" * 50)
length = random.randint(1, 20)  # 배열 길이
temp_celsius = np.array([random.uniform(-20, 70) for _ in range(length)]).round(1)
print(f"섭씨 센서값 배열\n{temp_celsius}")
temp_Fahrenheit = (temp_celsius * 9 / 5 + 3).round(1)
print(f"화씨 센서값 배열\n{temp_Fahrenheit}")
print("-" * 50)


print("\n\n" + "=" * 50)
print("=== 실습 2 - 균등 간격 배열 만들기 ===")
print("=" * 50)
length = random.randint(1, 20)  # 배열 길이
np_linspace = np.linspace(0, 100, 20)
print(f"np_linspace(0부터 100까지 균등 간격 20): {np_linspace}")
print("-" * 50)


print("\n\n" + "=" * 50)
print("=== 실습 3 - 측정 시간축 배열 만들기 ===")
print("=" * 50)
start, end = 0, 10  # 0초부터 10초까지 측정
interval = 2  # 2초 간격
time_axis = np.arange(start, end, interval)
print(f"시간축 (간격 {interval}초): {time_axis}, 개수: {time_axis.size}")

interval = 0.5  # 간격을 0.5초로 바꿔보기
time_axis = np.arange(start, end, interval)
print(f"시간축 (간격 {interval}초): {time_axis}, 개수: {time_axis.size}")
print("-" * 50)

print("\n\n" + "=" * 50)
print("=== 실습 4 - 배열 구조 확인하기 ===")
print("=" * 50)
equip_data = np.array([[random.randint(-20, 70) for _ in range(3)] for _ in range(2)])
print(f"설비 측정값\n{equip_data}")
print(f"차원(ndim): {equip_data.ndim}")
print("-" * 50)

print("\n\n" + "=" * 50)
print("=== 실습 6 - 배열 모양 바꾸기 ===")
print("=" * 50)
length = random.randint(1, 10) * 4
arr_1d = np.array([random.randint(0, 20) for _ in range(length)])
print(f"한 줄 배열 arr_1d = {arr_1d}")

arr_2d = arr_1d.reshape(-1, 4)
print(f"arr_2d 모양\n {arr_2d.shape}\n{arr_2d}")
print("-" * 50)
