# ========================================================
# 실습 1 - head/tail로 디지털 신호 살펴보기
print("=== 실습 1 - head/tail로 디지털 신호 살펴보기 ===")
import pandas as pd, os

file_1 = os.path.join("Data", "12_metro_digital.csv")

df_1 = pd.read_csv(file_1)

print(df_1.head(10), "\n", df_1.tail(10))


# ========================================================
# 실습 2 - head/tail 행 개수 조절
print("\n=== 실습 2 - head/tail 행 개수 조절 ===")
df_2 = pd.read_csv(
    "Data/12_metro_compressor.csv",
    encoding="utf-8",
    sep=",",
)
print(f"head(1):\n{df_2.head(1)}")
print(f"head(10):\n{df_2.head(10)}")
print(f"tail(7):\n{df_2.tail(7)}")
print(f"head(500):\n{df_2.head(500)}")

# ========================================================
# 실습 3 - 구조 파악 3종 도구
print("\n=== 실습 3 - 구조 파악 3종 도구 ===")
df_3 = pd.read_csv("Data/12_metro_digital.csv", sep=",", encoding="utf-8")
print(f"df_3.shape: {df_3.shape}")
print(f"df_3.columns: {df_3.columns}")
print(f"df_3.dtypes:\n{df_3.dtypes}")
print(
    "데이터 120개가 4개의 항목으로 구분되고, 각항목은 측정시각/압축기/타워/저압스위치이며, 각각 자료형은 str/int/int/int이다."
)

# ========================================================
# 실습 4 - 열 이름, 자료형 점검
print("\n=== 열 이름, 자료형 점검 ===")
df_4 = pd.read_csv("Data/12_metro_compressor.csv", sep=",", encoding="utf-8")
cols = list(df_4.columns)
print(
    cols
)  # ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']

print(f"df_4.dtyps:\n{df_4.dtypes}")

print("1. 숫자로 계산할 열이 모두 숫자 자료형인가? -> O")
print("2. ID 등 글자 열이 글자 자료형인가? -> 측정시각: str / 가동상태:str O")
print(
    "3. 온도가 object로 나온다면 어떤 문제가 생기는지 설명:\n \
      판다스에서 데이터의 자료형이 object로 나오는 것은 문자로 저장되었다는 뜻이다. 온도가 문자라면 수학적인 통계를 낼 수 없다."
)


# ========================================================
# 실습 5 - info로 데이터 건강검진
print("\n=== 실습 5 - info로 데이터 건강검진 ===")
df_5 = pd.read_csv("Data/12_metro_digital.csv", sep=",", encoding="utf-8")
print(f"df_5.info:\n{df_5.info()}")


# ========================================================
# 실습 6 - describe로 이상 신호 찾기
print("\n=== 실습 6 - describe로 이상 신호 찾기 ===")
df_6 = pd.read_csv("Data/12_metro_compressor.csv", sep=",", encoding="utf-8")
cols = list(df_6.columns)
print("데이터파일: Data/12_metro_compressor.csv")
print(f"df_6.describe():\n{df_6.describe()}")
print(f"오일 온도 평균과 최댓값 차이: {6.19 - 2.060850}")
print(f"75%와 max 차이가 큰 열 두 개 이상 찾았는가: 배출압력, 모터전류")
print(
    f"모터전류처럼 고른 열과 비교해 차이를 설명: 모터전류가 고르다고 생각하지 않는다."
)
