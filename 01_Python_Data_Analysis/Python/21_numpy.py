# 넘파이란?
# 다양한 외부 라이브러리를 가져오려면 pypi.org 사이트에서 검색부터 해야함
# 파이썬을 설치하면 파이썬 라이브러리 곤리 매니저인 pip도 생긴다.

# 터미널에서 바로 pip로 설치를 시도하면
# 전체 시스템에 영향을 주는 설치로 설치되어 거절당함
# 그래서 개발 Working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리를 따로 받아 쓰게 한다.
# 그게 바로 가상환경

# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가상환경 활성화
# source .venv/bin/activate

# 3. [작업 / 실행 끝나고) 가상환경 종료]
# deactivate

import numpy as np

# 위 intr값들의 리스트를ㅈ니하개 정하라

numbers = [1, 2, 3, 4, 5]
np_numbers = np.array(numbers)
print(np_numbers)


# 배열 생성 함수
# np.array(리스트): 값을 이미 알 때 / 소수점 하나라도 섞이면 float이 된다
temp = np.array([70.5, 69.8, 73.7])
print(f"temp: {temp} / temp.dtype: {temp.dtype}")


# np.arange(시작, 끝, 간격): 간격이 중요할 때 / 끝 값은 제외된다.
np_arange = np.arange(0, 12, 2)
print(f"np_arange: {np_arange} / np_arange.dtype: {np_arange.dtype},")
np_arange_10 = np.arange(10)
print(f"np_arnage_10: {np_arange_10} / np_arnage_10.ndim: {np_arange_10.ndim}")

# np.linspace(시작, 끝, 개수): 개수로 나눌 때 / 끝 값 포함, 인자는 간격이 아니라 점의 개수다!
np_linspace = np.linspace(0, 10, 23)
print(f"np_linspace(0,10,23): {np_linspace}")

# np.zeros(n): 0으로 채운 빈 그릇 / 결과를 담을 초기 배열
np_zeros = np.zeros(3, int)
print(np_zeros)

# np.full(n, 값): 값으로 채움
np_full = np.full(10, 10)
print(f"np_full(10, 10): {np_full} / np_full.dtype: {np_full.dtype}")


# 08.11 numpy 이틀차
import random

arr_a = np.array([[random.randint(1, 20) for _ in range(5)] for _ in range(3)])
print(f"arr_a:\n{arr_a}")
print(arr_a.shape)

rpm = np.array([[random.randint(1000, 5000) for _ in range(10)] for _ in range(5)])
print(f"rpm = \n {rpm}")
print("[0], [-1] 결과:\n", rpm[0], "\n", rpm[-1])
print("[0:5] 결과:\n", rpm[0:5])
print("[0][2] 결과:\n", rpm[0][2])

# numpy 배열 비교
# 비교한다라는 것이, bool type을 낸다는 걸 생각해보자
# 그 값들이 배열로 만들어지게끔 하는데, 왜 그렇게할까? 등호를 사용하여
# 비교하는 일을 개별적인 배열의 항목들을 꺼내어 차곡차곡 새로운 배열에 TRUE FALSE로 심어볼 수 있다.

compare = np.array([random.randint(0, 100) for _ in range(10)])
print(f"compare array: {compare}")
print(compare > 70)

print(compare[compare > 70])

# np.where
# 조건에 따라 값을 둘 중 하나로 바꾸기 - 조건/참/거짓 ... 세 가지 인자
print(np.where(compare > 85, 1, 0))  # 85보다 클 때, 1을, 작을 떄 0을 배열로 표현하기
compare_over = compare[compare > 70]
compare2 = compare_over[compare < 90]
print(compare2)


# 회전 수와 토크 배열 준비
import random, numpy as np

rpm = np.array([random.randint(1000, 5000) for _ in range(10)])
torque = np.array([random.uniform(0, 70) for _ in range(10)]).round(1)
print(f"rpm 배열:\n", rpm)
print(f"torque 배열:\n", torque)

# 비교 연산으로 회전 수가 기준을 넘는 조건 생성 -> 3000 이상으로 해보자
print("\nrpm 3000이상:", rpm[rpm > 3000])

# 다중 조건으로 회전수 과다 또는 토크 과서 위험 시점 필터링
# rpm[0] 데이터와 torque[0] 데이터는 같은 시기의 상황을 다룬다
print((rpm > 3000) | (torque < 10))


# 1차원 인덱싱 - 번호로 값 꺼내기

# 배열의 인덱스 번호는 파이썬 리스트처럼 0부터 시작

import random
import numpy as np

temp_rand = np.array([random.uniform(-20, 70) for _ in range(20)]).round(1)
print(f"온도 np.array: {temp_rand}")

# 첫 번째 내용만
print("첫 번째 인덱스", temp_rand[0])

# 끝
print("마지막 인덱스", temp_rand[-1])


temp_2d_rand = np.array(
    [[random.uniform(-20, 70) for _ in range(10)] for _ in range(random.randint(1, 5))]
).round(1)
print(f"temp_2d_rand:\n{temp_2d_rand}")

row = len(temp_2d_rand)
col = len(temp_2d_rand[0])
