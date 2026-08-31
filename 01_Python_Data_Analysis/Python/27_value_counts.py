###############################################################################
# 교안 14_01 - 빈도 집계 (value_counts, pd.cut)
# 교수님 설명 코드 (실습은 Practice/14_01_example.py)
###############################################################################

# value counts 기본 코드

import pandas as pd

df = pd.read_csv("Data/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head(3))

df_old = df[df["냉각기상태"] == "고장"]
print(len(df_old))  # 40
# 하지만 이 방식으로 모든 상태를 일일이 찾아서 통계내는 것은 비효율적
# '고장'외에도 모든 경우를 한번에 모아서 경우마다의 나타나는 갯수를 찾기
# value_counts

# 냉각기상태별 사이클 건수 세기
print(df["냉각기상태"].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40

# results 컬럼의 정상/고장 건수 세기
print(df["result"].value_counts())
# result
# 정상    67
# 고장    53

# 케이스마다 갯수 말고 비율로 알아보기
# 정규화 (normalize)
print(df["result"].value_counts(normalize=True))
# result
# 정상    0.558333
# 고장    0.441667

# 정규화 비율 결과를 위와 같이 쓰기보다는 round 처리로 반올림 할때가 많다
print(df["result"].value_counts(normalize=True).round(3))
# result
# 정상    0.558
# 고장    0.442

# pd.cut 구간 빈도 코드


df = pd.read_csv("Data/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head(3))

print(df["온도"].value_counts())
# 위와 같이 범위 없이 개별 경우의 수를 따져면 62가지나 되버린다
# 그래서 범위를 설정해 경우의 수를 줄여보기 -> 범주화
# ── [개념] pd.cut 으로 수치형을 구간으로 묶어 세기 ──────────────────────────
# 형식: pd.cut(df['수치열'], bins=[경계...], labels=[이름...])  → 구간 라벨 Series
# 엣지: 경계(bins)는 이름표(labels)보다 반드시 하나 많아야 함(경계 4개 → 구간 3개).
band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"])
print(band.value_counts())
# 온도
# 낮음    41
# 보통    40
# 높음    39


###############################################################################
# Source: 14_01_06_count-size_51_260819_1.py
###############################################################################


import pandas as pd

# 어제까지 배운 groupby 다시 살펴보기
df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')

# groupby로 냉각기상태마다 평균 온도 - 소숫점이하 2자리
print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89

# groupby로 운전부하마다 평균 진동 - 소숫점이하 3자리
print(df.groupby('운전부하')['진동'].mean().round(3))
# 운전부하
# 고부하    0.602
# 저부하    0.629

# 냉각기상태별로 다시 운전부하별 그룹을 나누어 평균 온도 
print(df.groupby(['냉각기상태', '운전부하'])['온도'].mean().round(2))
# 냉각기상태  운전부하
# 고장     고부하     55.51
#        저부하     54.05
# 저하     고부하     44.07
#        저부하     45.58
# 정상     고부하     35.89

# 냉각기상태별로 얼마나 많은 항목이 있을까?
print(len(df[df['냉각기상태'] == '고장'])) # 40
# 위 코드처럼 각 상태별로 갯수를 따로따로 계산하는 것은 비효율적 - size 활용
print(df.groupby('냉각기상태').size())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40
