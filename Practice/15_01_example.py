import pandas as pd
import os

###############################################################################
# 실습 1 - 눈으로 결측 찾기
###############################################################################
print("=" * 150, "\n", "=== 실습 1 - 눈으로 결측 찾기 ===")
path_1 = os.path.join("Data", "15_사출성형_로그.csv")
df_1 = pd.read_csv(path_1, encoding="utf-8")

# 설비 센서 데이터를 불러와 앞부분과 구조 확인
print("-" * 150)
print("설비 센서 데이터를 불러와 앞부분과 구조 확인:\n")
print(df_1.info())
print(df_1.head())

# isna로 컬럼별 NaN 개수 세기
# isna()는 True/False 표를 만들고, sum()이 True를 1로 더해줌
print("-" * 150)
print("isna로 컬럼별 NaN 개수 세기")
print(df_1.isna().sum())
print("전체 NaN 개수:", df_1.isna().sum().sum())

# 조건 필터링으로 위장 결측 개수 세기
# 위장 결측 = 값이 비어 있진 않지만 센서 오류를 뜻하는 특수값 (0, -999, 999 등)
print("-" * 150)
print("조건 필터링으로 위장 결측 개수 세기")
print("사출압력 == 0.0 :", (df_1["사출압력"] == 0.0).sum())
print("스크루속도 == -999.0 :", (df_1["스크루속도"] == -999.0).sum())
print("배럴온도 == 999.0 :", (df_1["배럴온도"] == 999.0).sum())

# 진짜 결측과 위장 결측을 나눠 비교
# 진짜 결측(NaN) 5개는 isna로 바로 잡히지만
# 위장 결측 5개(압력0 2개 + 속도-999 2개 + 온도999 1개)는 isna에 안 잡힘
print("-" * 150)
print("진짜 결측과 위장 결측을 나눠 비교")
real_na = df_1.isna().sum().sum()
fake_na = (
    (df_1["사출압력"] == 0.0).sum()
    + (df_1["스크루속도"] == -999.0).sum()
    + (df_1["배럴온도"] == 999.0).sum()
)
print("진짜 결측(NaN):", real_na, "|위장 결측:", fake_na, "|합계:", real_na + fake_na)


###############################################################################
# 실습 2 - 공정 데이터 첫 탐색
###############################################################################
print("=" * 150, "\n", "=== 실습 2 - 공정 데이터 첫 탐색 ===")
path_2 = os.path.join("Data", "15_01_사출성형_공정.csv")
df_2 = pd.read_csv(path_2, encoding="utf-8")

# read_csv로 불러와 head와 shape로 크기 확인
print("-" * 150)
print("head와 shape로 크기 확인")
print(df_2.head())
print("shape:", df_2.shape)

# info로 컬럼별 채워진 값 개수 훑기
# Non-Null Count가 전체 행 수(250)보다 작으면 그 컬럼에 결측이 있다는 뜻
print("-" * 150)
print("info로 컬럼별 채워진 값 개수 훑기")
print(df_2.info())

# describe의 count로 결측 있는 컬럼 짐작
# count는 결측을 뺀 개수라서, 250보다 작은 열이 곧 결측 있는 열
print("-" * 150)
print("describe의 count로 결측 있는 컬럼 짐작")
print(df_2.describe())

# 결측이 있는 컬럼만 추려서 확인
# 뒤쪽 센서 컬럼일수록 채워진 수가 줄어드는 패턴이 보임
print("-" * 150)
print("결측이 있는 컬럼만 추려서 내림차순 확인")
na_count_2 = df_2.isna().sum()
print(na_count_2[na_count_2 > 0].sort_values(ascending=False))


###############################################################################
# 실습 3 - 위장 결측 사냥
###############################################################################
print("=" * 150, "\n", "=== 실습 3 - 위장 결측 사냥 ===")
path_3 = os.path.join("Data", "15_사출성형_로그.csv")

# 변환 전 - 그냥 불러오기
df_before = pd.read_csv(path_3, encoding="utf-8")

# 위장 결측이 있는 열을 조건 필터링으로 추출해 확인
print("-" * 150)
print("변환 전 - 위장 결측이 있는 열을 조건 필터링으로 확인")
print("배럴온도 == 999.0 :", (df_before["배럴온도"] == 999.0).sum())
print("스크루속도 == -999.0 :", (df_before["스크루속도"] == -999.0).sum())
print("NaN 개수:", df_before.isna().sum().sum())

# na_values로 위장값을 결측으로 인식해 다시 불러오기
print("-" * 150)
print("na_values로 위장값을 결측으로 인식해 다시 불러오기")
df_after = pd.read_csv(path_3, encoding="utf-8", na_values=[-999, 999])
print("배럴온도 == 999.0 :", (df_after["배럴온도"] == 999.0).sum())
print("스크루속도 == -999.0 :", (df_after["스크루속도"] == -999.0).sum())
print("NaN 개수:", df_after.isna().sum().sum())

# 변환 전후 결측 개수를 비교
# -999, 999가 NaN으로 바뀌면서 5개 -> 8개로 늘어남
print("-" * 150)
print("변환 전후 컬럼별 결측 개수 비교")
compare_3 = pd.DataFrame(
    {
        "변환전": df_before.isna().sum(),
        "변환후": df_after.isna().sum(),
    }
)
compare_3["증가"] = compare_3["변환후"] - compare_3["변환전"]
print(compare_3)

# na_values로 다 잡히지 않는 위장 결측도 있음
# 사출압력의 0.0은 na_values에 안 넣었으므로 그대로 남아 있음
# 0이 진짜 측정값일 수도 있어서 도메인 판단이 필요한 부분
print("-" * 150)
print("na_values로 안 잡힌 위장 결측 확인")
print("변환 후에도 남은 사출압력 == 0.0 :", (df_after["사출압력"] == 0.0).sum())


###############################################################################
# 실습 4 - 결측 비율 계산
###############################################################################
print("=" * 150, "\n", "=== 실습 4 - 결측 비율 계산 ===")
path_4 = os.path.join("Data", "15_01_사출성형_공정.csv")
df_4 = pd.read_csv(path_4, encoding="utf-8")

# isna().mean()으로 컬럼별 결측 비율 구하기
# isna()가 True/False라서 mean()을 쓰면 True 비율 = 결측률이 됨
print("-" * 150)
print("isna().mean()으로 컬럼별 결측 비율 구하기")
na_rate_4 = df_4.isna().mean()
print(na_rate_4[na_rate_4 > 0].round(3))

# 100을 곱해 퍼센트로 바꾸고 내림차순 정렬
print("-" * 150)
print("퍼센트로 바꿔 결측률이 높은 컬럼 순으로 정렬")
na_pct_4 = (df_4.isna().mean() * 100).round(1)
print(na_pct_4[na_pct_4 > 0].sort_values(ascending=False))

# 개수와 비율을 한 표로 묶어 정리
print("-" * 150)
print("결측 개수와 비율을 한 표로 정리")
report_4 = pd.DataFrame(
    {
        "결측수": df_4.isna().sum(),
        "결측률(%)": (df_4.isna().mean() * 100).round(1),
    }
)
report_4 = report_4[report_4["결측수"] > 0].sort_values("결측률(%)", ascending=False)
print(report_4)

# 기준선을 정해 처리 우선순위 나누기
# 결측률 40% 이상이면 컬럼 자체를 쓸지 말지 판단해야 하는 수준
print("-" * 150)
print("결측률 40% 이상인 컬럼 (사용 여부 재검토 대상)")
print(report_4[report_4["결측률(%)"] >= 40])


###############################################################################
# 실습 5 - 행 단위 결측 패턴 확인
###############################################################################
print("=" * 150, "\n", "=== 실습 5 - 행 단위 결측 패턴 확인 ===")
path_5 = os.path.join("Data", "15_01_사출성형_공정.csv")
df_5 = pd.read_csv(path_5, encoding="utf-8")

# axis=1로 방향을 바꿔 행마다 결측이 몇 개인지 세기
print("-" * 150)
print("행마다 결측이 몇 개인지 세기")
na_per_row = df_5.isna().sum(axis=1)
print(na_per_row.head(10))

# 결측이 하나라도 있는 행과 완전한 행 세기
# any(axis=1)은 그 행에 True가 하나라도 있으면 True
print("-" * 150)
print("결측이 하나라도 있는 행과 완전한 행 비교")
print("전체 행 수:", len(df_5))
print("결측 있는 행 수:", df_5.isna().any(axis=1).sum())
print("완전한 행 수:", (~df_5.isna().any(axis=1)).sum())
print("완전한 행 비율(%):", round((~df_5.isna().any(axis=1)).mean() * 100, 1))

# 행별 결측 개수의 분포 확인
# 결측이 특정 행에 몰려 있는지, 골고루 퍼져 있는지 판단
print("-" * 150)
print("행별 결측 개수의 분포 확인")
print(na_per_row.value_counts().sort_index())

# 불량여부 그룹별로 결측 상황이 다른지 비교
# 결측이 특정 그룹에 쏠려 있으면 단순 누락이 아니라 원인이 있을 수 있음
print("-" * 150)
print("불량여부 그룹별 평균 결측 개수 비교")
df_5["행결측수"] = na_per_row
print(
    df_5.groupby("불량여부")
    .agg(
        행수=("행결측수", "count"),
        평균결측수=("행결측수", "mean"),
        최대결측수=("행결측수", "max"),
    )
    .round(2)
)

# [최종 정리]
# 발견 : 250행 중 174행(69.6%)에 결측이 있고, 완전한 행은 76행뿐
# 해석 : 계량종료점·감압시간이 43.6%로 결측률이 가장 높아 두 컬럼이 주범
# 행동 : 결측률 40% 이상 컬럼은 제거를 검토하고, 나머지는 15_02에서 대체값으로 채움
