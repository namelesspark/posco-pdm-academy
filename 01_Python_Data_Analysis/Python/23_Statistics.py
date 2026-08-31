# ===== 통계가 왜 필요한가 =====
# 수만개의 값을 일일이 볼 수 없다. 몇개의 대표 숫자로 요약해야함
# 평균이 얼마인지, 값이 얼마나 흔터졌는지 데이터의 특징을 한눈에 볼 수 있음
# 정상을 알아야 이상을 안다!
# ===== 주요 통계가 알려주는 것 =====
# 각 통계는 데이터의 다른 측면을 보여준다
# - 평균, 최대/최소, 표준 편차

# ===== 합계와 평균 =====
import random, numpy as np

s = np.array([random.randint(10, 100) for _ in range(5)])
print("s배열", s)
print("합계", s.sum())
print("평균", s.mean())

# ===== 평균의 약점 =====
# 평균만으로 판단하면 오해 발생함. 다른 통계와 함께 봐야함. 편차가 큰 값에 휘둘리게 된다.

# ===== 중앙값(median) =====
# 값을 줄 세웠을 때 한 가운데 오는 값
find_median = np.array([random.randint(10, 100) for _ in range(10)])

# 이상한 값 하나 추가해보자.
try:
    find_median = np.insert(find_median, random.randint(0, len(find_median)), 500)
except Exception as e:
    print(f"에러가 발생했습니다: {e}")

print("find_median:", find_median)
print("find_median 중앙값", np.median(find_median))
print("find_median 평균값", np.mean(find_median).round(1))

# ===== 분산 =====
# 값들이 평균에서 어느정도 흩어져 있는가를 숫자로 나타내는 것.
# 분산이 갑자기 커지면 이상 신호인 것 -> 작으면 안정, 커지면 불안정
# 값을 제곱해 구하기 때문에, 단위가 달라진다
stable = np.array([random.randint(1, 100) for _ in range(10)])
unstable = np.insert(stable, random.randint(0, len(stable)), 200)

print(f"stable: {stable}")
print(f"unstable: {unstable}")
print(f"stable 분산: {round(stable.var(), 1)}")
print(f"unstable 분산: {round(unstable.var(), 1)}")

# ===== 표준편차 =====
# 분산의 제곱근 - 원래 단위로 흩어진 정도를 표현하는 것.
print(f"stable 표준편차: {round(stable.std())}")
