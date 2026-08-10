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
print(f"행 길이: {row} / 열 길이: {col}")
