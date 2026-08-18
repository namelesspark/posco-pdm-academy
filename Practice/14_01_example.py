import pandas as pd
import os

###############################################################################
# 실습 1 - value_counts로 빈도 세기
###############################################################################
print("=" * 150, "\n", "=== 실습 1 - value_counts로 빈도 세기 ===")
path_1 = os.path.join("Data", "14_hydraulic.csv")
df_1 = pd.read_csv(path_1, encoding="utf-8")

# 설비 데이터를 불러와 앞부분과 구조 확인
print("-" * 150)
print("설비 데이터를 불러와 앞부분과 구조 확인:\n")
print(df_1.info())
print(df_1.head())

# 설비 열(컬럼)에 value_counts를 붙여 값별 개수 세기
# 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print("-" * 150)
print("설비 열(컬럼)에 value_counts를 붙여 값별 개수 세기")

for col in list(df_1.columns):
    print(df_1[col].value_counts())


###############################################################################
# 실습 2 - 비율과 불균형 데이터
###############################################################################
print("=" * 150, "\n", "=== 실습 2 - 비율과 불균형 데이터 ===")
path_2 = os.path.join("Data", "14_hydraulic_qc.csv")
df_2 = pd.read_csv(path_2, encoding="utf-8")

print(df_2.head())
# 공정 데이터의 판정 열에 value_counts로 합격·불합격 개수 세기
print(
    "공정 데이터의 판정 열에 value_counts로 합격·불합격 개수 세기\n",
    df_2["검사결과"].value_counts(),
)

# normalize 옵션으로 각 값의 비율을 소수로 확인
print(
    "normalize 옵션으로 각 값의 비율을 소수로 확인\n",
    df_2["검사결과"].value_counts(normalize=True),
)


# round로 비율을 소수점 셋째 자리까지 정리
print(
    "round로 비율을 소수점 셋째 자리까지 정리",
    df_2["검사결과"].value_counts(normalize=True).round(1),
)


###############################################################################
# 실습 3 - 구간으로 묶어 세기
###############################################################################
print("=" * 150, "\n", "=== 실습 3 - 구간으로 묶어 세기 ===")
path_3 = os.path.join("Data", "14_hydraulic.csv")
df_3 = pd.read_csv(path_3, encoding="utf-8")

print(df_3.info(), df_3.head())
# 진동 열의 최솟값과 최댓값으로 값의 범위 확인
print(
    "-" * 150,
    "\n",
    "진동 열의 최솟값과 최댓값으로 값의 범위 확인",
    "max():",
    df_3["진동"].max(),
    "|min():",
    df_3["진동"].min(),
)
# pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기
# 묶은 구간에 value_counts로 구간별 빈도 세기
band = pd.cut(df_3["진동"], bins=[0.0, 0.6, 0.7, 10.0], labels=["약함", "보통", "강함"])
print(
    "-" * 150,
    "\n",
    "pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기",
    "\n",
    "묶은 구간에 value_counts로 구간별 빈도 세기",
)
print(band.value_counts())
