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
