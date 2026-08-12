import random
import numpy as np

# ========================================================================
# 실습 1 - 특정 센서 / 구간 추출하기
print("=== 실습 1 - 특정 센서 / 구간 추출하기 ===")
# 회전수 측정값 배열 준비
rpm = np.array([random.randint(1000, 5000) for _ in range(10)])
print(f"rpm 배열: {rpm}")

# 인덱싱으로 첫 시점과 마지막 시점 값 꺼내기
print(f"첫 시점: {rpm[0]} | 마지막 시점 {rpm[-1]}")

# 슬라이싱으로 앞 구간과 두 칸 간격 값 추출
print(f"슬라이싱으로 앞 구간과 두 칸 간격 값 추출: {rpm[::2]}")


# ========================================================================
# 실습 2 - 행 / 열 단위로 추출하기
print("\n=== 실습 2 - 행 / 열 단위로 추출하기 ===")
import os

np.set_printoptions(suppress=True)  # 지수 표기법 끄기

file_path = os.path.join("Data", "10_mct_tool.csv")

with open(file_path, "r", encoding="utf-8") as f:
    df = np.loadtxt(f, encoding="utf-8", delimiter=",", skiprows=1, usecols=(4, 5))
    print(f"df:\n{df}")
# ========================================================================
# 실습 4 - 이상 센서값 필터링하기
print("\n=== 실습 4 - 이상 센서값 필터링하기 ===")
rpm = np.array([random.randint(1000, 5000) for _ in range(10)])
torque = np.array([random.uniform(0, 70) for _ in range(10)]).round(1)
print("rpm 배열:\n", rpm)
print("torque 배열:\n", torque)

# 비교 연산으로 회전 수가 기준을 넘는 조건 생성 -> RPM 3000 이상, torque 10 이하
print(f"RPM 3000 이상: {rpm[rpm > 3000]}")

print(f"비교 연산으로 RPM 3000 이상, torque 10 이하]\n\
      {(rpm > 3000) | (torque < 10)}")

# ========================================================================
# 실습 7 - 파일 데이터로 기초 통계 구하기
print("\n=== 실습 7 - 파일 데이터로 기초 통계 구하기 ===")
import numpy as np

# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm = np.loadtxt(
    "Data/10_mct_tool.csv", encoding="utf-8", delimiter=",", skiprows=1, usecols=4
)

# 불러온 배열의 평균과 표준편차 계산
print(f"불러온 데이터:\n\
      {rpm}")
print(f"평균: {np.mean(rpm):.2f}")
print(f"표준편차: {np.std(rpm):.2f}")

# ========================================================================
# 실습 8 - 필터링과 통계 결합하기
print("\n=== 실습 8 - 필터링과 통계 결합하기 ===")
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산

torque = np.loadtxt(
    "Data/10_mct_tool.csv", encoding="utf-8", delimiter=",", skiprows=1, usecols=5
)

# 불리언 인덱싱으로 기준을 넘는 값만 추출
torque_over_5 = torque[torque > 5]
print(f"토크 5 초과 값: {torque_over_5}")

# 추출한 값들의 평균과 개수 계산
print(f"기준값 초과 개수: {len(torque_over_5)}")
print(f"기준값 초과 평균: {np.mean(torque_over_5)}")

# ========================================================================
# 실습 9 - Numpy 기초 종합 분석
np.set_printoptions(suppress=True)  # 지수 표기법 끄기
print("\n=== 실습 9 - Numpy 기초 종합 분석 ===")

# loadtxt로 회전수와 토크 두 열을 불러오기
rpm_and_torque = np.loadtxt(
    "Data/10_mct_tool.csv",
    encoding="utf-8",
    delimiter=",",
    skiprows=1,
    usecols=(4, 5),
    unpack=True,
)

# shape와 dtype으로 구조 확인
print(f"rpm_and_torque np.array:\n\
      {rpm_and_torque}")
print(f"rpn_and_torque.shape:\n\
      {rpm_and_torque.shape}")
print(f"rpn_and_torque.shape:\n\
      {rpm_and_torque.dtype}")

# 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
get_rpm = rpm_and_torque[0]
anomaly = get_rpm[get_rpm <= 1000]
print(anomaly)
print(
    f"get_rpm:\n{get_rpm}\nRPM 1000 이하:\n{anomaly}\n개수: {anomaly.size}\n평균: {anomaly.mean().round(1)}"
)
