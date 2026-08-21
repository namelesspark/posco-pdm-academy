import pandas as pd
import os

###############################################################################
# 실습 3 - 결측 비율 기준 컬럼 제거
###############################################################################
print("=" * 150, "\n", "=== 실습 3 - 결측 비율 기준 컬럼 제거 ===")
path_3 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_3 = pd.read_csv(path_3, encoding="utf-8")

# 데이터를 불러와 크기와 결측 현황 확인
print("-" * 150)
print("데이터를 불러와 크기와 결측 현황 확인")
print("shape:", df_3.shape)
na_count_3 = df_3.isna().sum()
print(na_count_3[na_count_3 > 0].sort_values(ascending=False))

# 컬럼별 결측 비율을 계산
# isna().sum()으로 개수를 세고 전체 행 수로 나누면 비율
print("-" * 150)
print("컬럼별 결측 비율을 계산")
na_rate_3 = df_3.isna().sum() / len(df_3)
print(na_rate_3[na_rate_3 > 0].round(3).sort_values(ascending=False))

# 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기 (기준: 40%)
# 조건 필터링 결과의 index가 곧 컬럼 이름이라 tolist()로 목록화
print("-" * 150)
print("결측 비율 40%를 넘는 컬럼만 목록으로 뽑기")
over_3 = na_rate_3[na_rate_3 > 0.4]
print(over_3.round(3))
drop_cols_3 = over_3.index.tolist()
print("제거 대상 컬럼:", drop_cols_3)

# 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 columns를 넘기면 열 방향으로 삭제됨
print("-" * 150)
print("drop으로 제거하고 크기 확인")
df_dropped_3 = df_3.drop(columns=drop_cols_3)
print("제거 전 shape:", df_3.shape, "-> 제거 후 shape:", df_dropped_3.shape)


###############################################################################
# 실습 4 - 삭제 손실 비교
###############################################################################
print("=" * 150, "\n", "=== 실습 4 - 삭제 손실 비교 ===")
path_4 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_4 = pd.read_csv(path_4, encoding="utf-8")

# 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# dropna()는 결측이 하나라도 있으면 그 행을 통째로 삭제
# dropna(thresh=20)은 값이 20개 이상 채워진 행만 남김
print("-" * 150)
print("삭제 방식별로 남는 행 수 구하기")
rows_origin = len(df_4)
rows_dropna = len(df_4.dropna())
rows_thresh = len(df_4.dropna(thresh=20))
print("원본:", rows_origin)
print("행삭제(dropna):", rows_dropna)
print("thresh=20:", rows_thresh)

# 방식과 행 수를 하나의 표로 모으기
# 원본 대비 손실률을 백분율로 계산해 나란히 보기
print("-" * 150)
print("방식별 남는 행 수와 손실률을 표로 정리")
compare_4 = pd.DataFrame(
    {
        "방식": ["원본", "행삭제", "thresh20"],
        "행수": [rows_origin, rows_dropna, rows_thresh],
    }
)
compare_4["손실률(%)"] = ((1 - compare_4["행수"] / rows_origin) * 100).round(2)
print(compare_4)

# 행삭제는 손실률 69.6%로 데이터의 3분의 2 이상이 날아감
# thresh는 35.2%로 손실이 절반 수준이지만 여전히 큼
# -> 삭제만으로는 데이터를 지키기 어려우니 대체(fillna)가 필요


###############################################################################
# 실습 5 - fillna 평균·중앙값 대체
###############################################################################
print("=" * 150, "\n", "=== 실습 5 - fillna 평균·중앙값 대체 ===")
path_5 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_5 = pd.read_csv(path_5, encoding="utf-8")

# 대상 컬럼의 결측 개수 확인
print("-" * 150)
print("대상 컬럼(최대사출압)의 결측 개수 확인")
print("NaN 개수:", df_5["최대사출압"].isna().sum())

# 대상 컬럼의 평균과 중앙값을 각각 구해 비교
# 두 값 모두 반드시 원본에서 구해야 함 (채운 뒤에 구하면 값이 오염됨)
print("-" * 150)
mean_5 = df_5["최대사출압"].mean()
median_5 = df_5["최대사출압"].median()
print(
    "평균과 중앙값을 각각 구해 비교",
    "\n",
    "mean():",
    round(mean_5, 3),
    "|median():",
    round(median_5, 3),
    "|차이:",
    round(mean_5 - median_5, 3),
)

# fillna로 평균을 채운 결과 만들기
print("-" * 150)
print("fillna로 평균을 채운 결과 만들기")
s_fill_mean = df_5["최대사출압"].fillna(mean_5)
print("채운 뒤 NaN 개수:", s_fill_mean.isna().sum())

# fillna로 중앙값을 채운 결과 만들기 (이상치에 강함)
print("-" * 150)
print("fillna로 중앙값을 채운 결과 만들기")
s_fill_median = df_5["최대사출압"].fillna(median_5)
print("채운 뒤 NaN 개수:", s_fill_median.isna().sum())

# 두 방식의 결과를 통계로 비교
# 평균으로 채우면 평균이 그대로 유지되고, 중앙값으로 채우면 평균이 살짝 내려감
print("-" * 150)
print("두 대체 방식의 결과 비교")
compare_5 = pd.DataFrame(
    {
        "원본": df_5["최대사출압"].describe(),
        "평균대체": s_fill_mean.describe(),
        "중앙값대체": s_fill_median.describe(),
    }
).round(3)
print(compare_5)


###############################################################################
# 실습 6 - 최빈값·앞뒤 값 대체
###############################################################################
print("=" * 150, "\n", "=== 실습 6 - 최빈값·앞뒤 값 대체 ===")
path_6 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_6 = pd.read_csv(path_6, encoding="utf-8")

# 범주형 열의 최빈값을 구해 채우기
# 숫자가 아니라 평균을 못 쓰므로 가장 많이 나온 값(mode)으로 채움
# mode()는 Series를 반환하므로 [0]으로 첫 값을 꺼내야 함
print("-" * 150)
print("범주형 열(사출기)의 최빈값을 구해 채우기")
print("채우기 전 NaN 개수:", df_6["사출기"].isna().sum())
print("값 분포:\n", df_6["사출기"].value_counts())
print("최빈값 mode()[0]:", df_6["사출기"].mode()[0])
df_6["사출기"] = df_6["사출기"].fillna(df_6["사출기"].mode()[0])
print("채운 뒤 NaN 개수:", df_6["사출기"].isna().sum())

# 측정시각 순으로 정렬해 시계열 순서 만들기
# 앞뒤 값으로 채우려면 시간 순서가 먼저 맞아야 함
print("-" * 150)
print("측정시각 순으로 정렬해 시계열 순서 만들기")
df_6 = df_6.sort_values("측정시각")
print(df_6["측정시각"].head(3).tolist())

# ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
# ffill만 쓰면 맨 첫 행이 결측일 때 채울 앞 값이 없어 그대로 남음 -> bfill로 마무리
print("-" * 150)
print("ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기")
print("채우기 전 전환압력 NaN 개수:", df_6["전환압력"].isna().sum())
df_6["전환압력"] = df_6["전환압력"].ffill().bfill()
print("채운 뒤 전환압력 NaN 개수:", df_6["전환압력"].isna().sum())


###############################################################################
# 실습 7 - 그룹별 대체
###############################################################################
print("=" * 150, "\n", "=== 실습 7 - 그룹별 대체 ===")
path_7 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_7 = pd.read_csv(path_7, encoding="utf-8")

# 사출기로 그룹을 나눠 그룹별 평균이 다른지 확인
# 그룹마다 평균이 다르면 전체 평균 하나로 채우는 건 집단 특성을 뭉개는 것
print("-" * 150)
print("사출기로 그룹을 나눠 감압시간의 그룹별 평균 확인")
print(df_7.groupby("사출기")["감압시간"].mean().round(6))
print("전체 평균:", round(df_7["감압시간"].mean(), 6))

# 각 그룹의 평균으로 그 그룹의 결측을 채우기
# transform은 그룹별 계산 결과를 원래 행 위치에 그대로 돌려줌
print("-" * 150)
print("각 그룹의 평균으로 그 그룹의 결측을 채우기")
print("채우기 전 감압시간 NaN 개수:", df_7["감압시간"].isna().sum())
df_7["감압시간"] = df_7.groupby("사출기")["감압시간"].transform(
    lambda s: s.fillna(s.mean())
)
print("채운 뒤 감압시간 NaN 개수:", df_7["감압시간"].isna().sum())

# 남은 수치 결측은 전체 중앙값으로 마무리하고 검증
# select_dtypes("number")로 숫자 컬럼만 골라서 처리
# 실무에서는 컬럼 특성을 따지지 않고 한꺼번에 채우는 건 권장되지 않음
print("-" * 150)
print("남은 수치 결측을 전체 중앙값으로 마무리")
num_cols_7 = df_7.select_dtypes("number")
df_7[num_cols_7.columns] = num_cols_7.fillna(num_cols_7.median())
print("전체 남은 결측:", df_7.isna().sum().sum())


###############################################################################
# 실습 8 - 제거 vs 대체 비교
###############################################################################
print("=" * 150, "\n", "=== 실습 8 - 제거 vs 대체 비교 ===")
path_8 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_8 = pd.read_csv(path_8, encoding="utf-8")

# 결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기
print("-" * 150)
print("결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기")
base_8 = df_8.drop(columns=["최대사출속도", "감압시간"])
print("원본 shape:", df_8.shape, "-> 기준 shape:", base_8.shape)

# 기준 데이터에서 결측 행을 삭제한 제거 버전 만들기
print("-" * 150)
print("결측 행을 삭제한 제거 버전 만들기")
drop_8 = base_8.dropna()
print("제거판 shape:", drop_8.shape)

# 기준 데이터의 결측을 중앙값으로 채운 대체 버전 만들기
# numeric_only=True로 숫자 컬럼의 중앙값만 계산
print("-" * 150)
print("결측을 중앙값으로 채운 대체 버전 만들기")
fill_8 = base_8.fillna(base_8.median(numeric_only=True))
print("대체판 shape:", fill_8.shape)

# 두 버전을 표로 비교
print("-" * 150)
print("제거 버전과 대체 버전 비교")
compare_8 = pd.DataFrame(
    {
        "방식": ["기준", "제거판", "대체판"],
        "행수": [len(base_8), len(drop_8), len(fill_8)],
        "남은결측": [
            base_8.isna().sum().sum(),
            drop_8.isna().sum().sum(),
            fill_8.isna().sum().sum(),
        ],
    }
)
compare_8["보존율(%)"] = (compare_8["행수"] / len(base_8) * 100).round(1)
print(compare_8)

# 제거판은 110행만 남아 44%만 보존, 대체판은 250행 전부 보존
# 대신 대체판은 채운 값이 실제 측정값이 아니라는 점을 감안해야 함


###############################################################################
# 실습 9 - 종합 처리와 저장
###############################################################################
print("=" * 150, "\n", "=== 실습 9 - 종합 처리와 저장 ===")
path_9 = os.path.join("Data", "15_02_사출성형_공정.csv")
df_9 = pd.read_csv(path_9, encoding="utf-8")

# 결측 비율 높은 컬럼을 제거하고 나머지는 중앙값으로 채우기
# 실습 3(컬럼 제거) + 실습 5(중앙값 대체)를 하나의 흐름으로 연결
print("-" * 150)
print("결측 비율 40% 초과 컬럼 제거")
na_rate_9 = df_9.isna().sum() / len(df_9)
drop_cols_9 = na_rate_9[na_rate_9 > 0.4].index.tolist()
print("제거 대상:", drop_cols_9)
clean_9 = df_9.drop(columns=drop_cols_9)
print("제거 후 shape:", clean_9.shape)

print("-" * 150)
print("남은 결측을 중앙값으로 채우기")
print("채우기 전 결측:", clean_9.isna().sum().sum())
clean_9 = clean_9.fillna(clean_9.median(numeric_only=True))
print("채운 뒤 결측:", clean_9.isna().sum().sum())

# 처리 후 남은 결측과 크기를 확인하고 파일로 저장
print("-" * 150)
print("처리 결과 확인 후 파일로 저장")
print("최종 shape:", clean_9.shape)
print("최종 남은 결측:", clean_9.isna().sum().sum())

out_path_9 = os.path.join("Data", "15_02_사출성형_공정_clean.csv")
clean_9.to_csv(out_path_9, index=False, encoding="utf-8")
print("저장 완료:", out_path_9)

# 저장한 파일을 다시 읽어 검증
print("-" * 150)
print("저장한 파일을 다시 읽어 검증")
check_9 = pd.read_csv(out_path_9, encoding="utf-8")
print("다시 읽은 shape:", check_9.shape, "|남은 결측:", check_9.isna().sum().sum())
