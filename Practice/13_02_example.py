# ====================================================
# 실습 1 - 단일 조건으로 행 추출하기
print("\n=== 실습 1 - 단일 조건으로 행 추출하기 ===")
# 조건을 만들고 그 조건으로 원하는 행만 추출
import pandas as pd
import os

path_1 = os.path.join("Data", "13_diecasting_shot.csv")
df_1 = pd.read_csv(path_1)
cols = list(df_1.columns)
# 1. 비교 연산자로 실린더압력 기준의 조건식을 만들어 Boolean Series 생성
mask_1 = df_1[cols[1]] >= 230
print(f"mask_1:\n{mask_1}")
# 2. sum으로 조건을 만족하는 행 개수 확인
print(f"sum으로 조건을 만족하는 행 개수 확인: {mask_1.sum()}")
print("-" * 50)
# 3. 만든 조건을 데이터프레임 대괄호에 넣어 행 추출
print(f"행 추출:\n{df_1[mask_1]}")
print("-" * 50)

# ====================================================
# 실습 2 - 임계값 넘는 설비 골라내기
print("\n=== 실습 2 - 임계값 넘는 설비 골라내기 ===")
path_2 = os.path.join("Data", "13_diecasting_shot.csv")
df_2 = pd.read_csv(path_2)
cols = list(df_1.columns)
print(cols)
print("-" * 50)
# 1. 비스킷두께 열에 비교 연산자로 임계값 기준 조건 생성
mask_2 = df_2[cols[4]] > 16
print(f"mask_2:\n{mask_2}")
print("-" * 50)
# 2. 조건을 대괄호에 넣어 임계값 초과 설비만 추출
print(f"비스킷두께 16 초과 설비:\n{df_2[mask_2]}")
print("-" * 50)
# 3. 결과에서 샷과 비스켓두께 열만 골라 확인
mask_2_2 = df_2.loc[mask_2, ["샷", "비스킷두께"]]
print(f"샷, 비스킷두께 확인:\n{mask_2_2}")
print("-" * 50)


# ====================================================
# 실습 3 - 두 조건 묶기
print("\n=== 실습 3 - 두 조건 묶기 ===")
path_3 = os.path.join("Data", "13_diecasting_shot.csv")
df_3 = pd.read_csv(path_3, encoding="utf-8")
print(f"컬럼 리스트:\n{list(df_3.columns)}")
df_3.info()

print(
    f"비스킷두께:\n{df_3['비스킷두께'].describe()}\n사이클타임:\n{df_3['사이클타임'].describe()}"
)
# 1. 비스킷두께 조건과 사이클타임 조건을 각각 괄호로 감싸기

print("-" * 50)
df_3_1 = df_3[df_3["비스킷두께"] >= 13]
print(f"df_3_1 len: {len(df_3_1)}")

print("-" * 50)
df_3_2 = df_3[df_3["사이클타임"] >= 22]
print(f"df_3_2 len: {len(df_3_2)}")

# 2. 두 조건을 그리고 기호로 묶어 모두 만족하는 행 추출
df_3_both_and = df_3[(df_3["비스킷두께"] >= 13) & (df_3["사이클타임"] >= 22)]
print("-" * 50)
print(f"비스킷두께, 사이클타임 모두 만족만족:\n{df_3_both_and.describe()}")

# 3. 같은 두 조건을 또는 기호로 묶어 결과 수 비교
df_3_both_or = df_3[(df_3["비스킷두께"] >= 13) | (df_3["사이클타임"] >= 22)]
print("-" * 50)
print(f"df_3_both_and 길이: {len(df_3_both_and)}")
print("-" * 50)
print(f"df_3_both_or 길이: {len(df_3_both_or)}")

# ====================================================
# 실습 4 - 부정 / 목록 / 범위 조건
print("\n=== 실습 4 - 부정 / 목록 / 범위 조건 ===")
path_4 = os.path.join("Data", "13_diecasting_shot.csv")
df_4 = pd.read_csv(path_3, encoding="utf-8")


# 1. 물결 기호로 고장이 아닌 설비만 뒤집어 추출
print("-" * 50)
print(df_4.tail())
print(df_4[df_4["품질등급"] == "불량"].head())

print("-" * 50)
print(f"불량 아닌 것:\n\
      {df_4[ ~(df_4["품질등급"] == "불량")].head()}")

# 2. isin으로 품질등급이 특정 목록에 속하는 행 추출
print("-" * 50)
print(df_4["품질등급"].unique())
print(df_4[df_4.isin(["양품", "주의"])])
print(len(df_4[df_4.isin(["양품", "주의"])]))

# 3. between으로 실린더압력가 지정 범위에 든 행 추출
print("-" * 50)
print(df_4[df_4["실린더압력"].between(210, 230)].head())
print(len(df_4[df_4["실린더압력"].between(210, 230)]))


# ====================================================
# 실습 5 - 위험 순으로 정렬하기
print("\n=== 실습 5 - 위험 순으로 정렬하기 ===")
path_5 = os.path.join("Data", "13_diecasting_shot.csv")
df_5 = pd.read_csv(path_5, encoding="utf-8")

# 1. sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
print("-" * 50)
df_5_sorted_biscuit = df_5.sort_values("비스킷두께", ascending=False)
print(f"비스킷두께로 내림차순 정렬:\n\
      {df_5_sorted_biscuit}")

# 2. head로 상위 다섯 개만 추출해 값 확인
print("-" * 50)
print(f"head 상위:\n\
      {df_5_sorted_biscuit.head()}")

# 3. 여러 열을 리스트로 묶어 우선순위 다중 정렬
print("-" * 50)
df_5_sorted_multi = df_5.sort_values(
    by=["비스킷두께", "실린더압력"], ascending=[False, False]
)
print(f"비스킷두께, 실린더압력으로 우선순위 내림차순 정렬:\n\
      {df_5_sorted_multi.head()}")

# ====================================================
# 실습 6 - 필터링과 정렬 연결
print("\n=== 실습 6 - 필터링과 정렬 연결 ===")
path_6 = os.path.join("Data", "13_diecasting_shot.csv")
df_6 = pd.read_csv(path_6, encoding="utf-8")

# 1. 고장 여부 조건으로 고장 설비만 먼저 고르기
print(list(df_6.columns))
found_col = None
for col in df_6.columns:
    if "고장" in df_6[col].unique():
        found_col = col
        break

print("-" * 50)
if found_col:
    print(f"'고장' 값이 있는 컬럼명: {found_col}")
else:
    print("'고장' 값을 가진 컬럼은 없습니다.")
    print("'품질등급'의 '불량' 값을 기준으로 실습을 진행하겠습니다.")


df_6_defective = df_6[df_6["품질등급"] == "불량"]

# 2. 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
df_6_sorted_defective = df_6_defective.sort_values("비스킷두께", ascending=False)
print(f"비스킷두께 정렬 데이터프레임:\n\
      {df_6_sorted_defective}")

# 3. head로 상위 다섯 개만 남겨 샷 확인
print("-" * 50)
print(f"샷만 남겨 head로 보기:\n\
      {df_6_sorted_defective[["샷","비스킷두께"]].head(5)}")
