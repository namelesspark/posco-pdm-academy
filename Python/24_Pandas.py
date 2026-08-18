import os, csv, numpy as np, pandas as pd

file_path = os.path.join("Data", "12_metro_small.csv")

try:
    df = pd.read_csv(file_path, sep=",", index_col="모터전류", encoding="utf-8")
except FileNotFoundError:
    print(f"file not found:{file_path}")

print(df.count(1))
print("-" * 50)
print(df.shape)


###############################################################################
# 13_02 필터링 & 정렬 - 교안 설명 코드
# (실습 5·6·7 은 Practice/13_02_example.py 로)
###############################################################################

# Pandas에서 원본에 변경을 주려면 꼭 .copy()를 하세요!
# 안그러면 SettingWithCopyWarning 경고 발생

import pandas as pd

df = pd.read_csv("Data/13_diecasting_shot.csv", encoding="utf-8")
df.info()

df_bad = df[df["품질등급"] == "불량"].copy()

# 만약 copy 없이 바로 df_bad의 모든 품질등급을 다른 내용으로 변경한다면? 경고가 발생할 수도 있음
df_bad["품질등급"] = "점검"

print(df_bad.head())
#        샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 180  181  108.0   522.0  652.3   14.0  222.0   점검
# 181  182  214.0  1036.0   93.1   12.0  247.0   점검
# 182  183  215.0  1041.0   21.3    4.0  258.0   점검
# 183  184  216.0  1044.0   21.2   11.0  259.0   점검
# 184  185  219.0  1058.0   21.3    2.0  255.0   점검

###############################################################################
# 14_01 빈도 집계 - 교안 설명 코드
# (실습 1·2·3 은 Practice/14_01_example.py 로)
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

import pandas as pd

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
