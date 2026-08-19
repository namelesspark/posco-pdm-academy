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


###############################################################################
# 실습 4 - groupby로 그룹 집계
###############################################################################
print("=" * 150, "\n", "=== 실습 4 - groupby로 그룹 집계 ===")
path_4 = os.path.join("Data", "14_hydraulic.csv")
df_4 = pd.read_csv(path_4, encoding="utf-8")

# 기준 → 열 → 함수 순으로 그룹별 통계 구하기
# 라인으로 그룹을 나눠 압력 열의 평균 집계 (라인 = 냉각기상태)
print("-" * 150)
print("라인으로 그룹을 나눠 압력 열의 평균 집계")
print(df_4.groupby("냉각기상태")["압력"].mean().round(2))

# 집계 함수를 바꿔 설비별 최고 온도 확인 (설비 = 밸브상태 / max, min)
print("-" * 150)
print("집계 함수를 바꿔 설비별 최고 온도 확인")
print(df_4.groupby("밸브상태")["온도"].max())

# size로 교대별 측정 건수까지 확인 (교대 = 운전부하)
# size는 결측(NaN)이 있어도 행 수를 그대로 세는 점이 value_counts와 다름
print("-" * 150)
print("size로 교대별 측정 건수까지 확인")
print(df_4.groupby("운전부하").size())


###############################################################################
# 실습 5 - 그룹별 평균 비교와 정렬
###############################################################################
print("=" * 150, "\n", "=== 실습 5 - 그룹별 평균 비교와 정렬 ===")
path_5 = os.path.join("Data", "14_hydraulic.csv")
df_5 = pd.read_csv(path_5, encoding="utf-8")

# 설비로 그룹을 나눠 진동 평균 집계
print("-" * 150)
print("설비로 그룹을 나눠 진동 평균 집계")
print(df_5.groupby("밸브상태")["진동"].mean().round(3))

# 집계 결과에 정렬을 이어 붙여 내림차순으로 정렬
# 가장 진동이 큰 설비를 맨 위에서 확인 (심각 > 지연 > 경미 > 정상)
print("-" * 150)
print("집계 결과에 정렬을 이어 붙여 내림차순으로 정렬")
print(df_5.groupby("밸브상태")["진동"].mean().round(3).sort_values(ascending=False))


###############################################################################
# 실습 6 - 여러 기준 조합 그룹
###############################################################################
print("=" * 150, "\n", "=== 실습 6 - 여러 기준 조합 그룹 ===")
path_6 = os.path.join("Data", "14_hydraulic.csv")
df_6 = pd.read_csv(path_6, encoding="utf-8")

# 라인과 교대 두 기준을 묶어 진동 평균 집계
# groupby에 리스트를 넘기면 적은 순서대로 그룹이 중첩됨
print("-" * 150)
print("라인과 교대 두 기준을 묶어 진동 평균 집계")
print(df_6.groupby(["냉각기상태", "운전부하"])["진동"].mean().round(3))

# 같은 두 기준으로 size를 구해 조합별 측정 건수 확인
# 건수가 적은 조합(저하-고부하 3건)의 평균은 신중히 해석할 것
print("-" * 150)
print("같은 두 기준으로 size를 구해 조합별 측정 건수 확인")
print(df_6.groupby(["냉각기상태", "운전부하"]).size())


###############################################################################
# 실습 7 - 빈도와 그룹 집계 종합
###############################################################################
print("=" * 150, "\n", "=== 실습 7 - 빈도와 그룹 집계 종합 ===")
path_7 = os.path.join("Data", "14_hydraulic.csv")
df_7 = pd.read_csv(path_7, encoding="utf-8")

# value_counts로 설비 구성과 정상·고장 비율 파악
# value_counts는 결측(NaN)을 세지 않음 (groupby size와의 차이)
print("-" * 150)
print("value_counts로 설비 구성 파악")
print(df_7["밸브상태"].value_counts())
print(df_7["밸브상태"].value_counts(normalize=True).round(3))

# 고장 행만 걸러 라인별 고장 건수 집계
# 아래 세 가지는 같은 53을 주지만 의미가 다름
#   len(불리언 인덱싱)  : 고장 행만 세어 딱 그 값만 반환 -> 문제에 가장 부합
#   groupby().size()   : 모든 값별 행 수를 한꺼번에 반환
#   value_counts()     : 모든 값별 빈도를 내림차순으로 반환
print("-" * 150)
print("고장 행만 걸러 고장 건수 집계")
print(len(df_7[df_7["result"] == "고장"]))
print(df_7.groupby("result").size())
print(df_7["result"].value_counts())

# groupby로 설비별 온도·진동 평균까지 비교
# 열을 리스트로 넘기면 두 열을 따로 집계하지 않고 한 번에 처리 가능
print("-" * 150)
print("groupby로 설비별 온도·진동 평균 비교")
print(df_7.groupby("냉각기상태")[["온도", "진동"]].mean().round(2))
