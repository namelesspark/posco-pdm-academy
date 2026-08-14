# ==================================================
# 실습 1 - 데이터 불러오기와 구조 확인하기
print("=== 실습 1 - 데이터 불러오기와 구조 확인하기 ===")
import pandas as pd

pd.set_option("display.width", 10000)
pd.set_option("display.max_columns", None)

df_1 = pd.read_csv("Data/13_diecasting_small.csv", sep=",", encoding="utf-8")
print(f"df_1:\n{df_1}")
print("-" * 50)
print(f"df_1.head(5):\n{df_1.head(5)}")
print("-" * 50)
print(f"df_1.columns:\n{df_1.columns}")
print("-" * 50)
print(f"df_1.shape:\n{df_1.shape}")

# ==================================================
# 실습 2 - 열 선택하기
print("\n=== 실습 2 - 열 선택하기 ===")
df_2_1 = pd.read_csv(
    "Data/13_diecasting_small.csv", sep=",", encoding="utf-8", usecols=["주조압력"]
)["주조압력"]

df_2_2 = pd.read_csv(
    "Data/13_diecasting_small.csv",
    sep=",",
    encoding="utf-8",
    usecols=["실린더압력", "주조압력", "사이클타임"],
)
print("-" * 50)
print(f"df_2_1.mean(): {df_2_1.mean()}")
print(f"type(df_2_1): {type(df_2_1)}")
print("-" * 50)
print(f"df_2_2.mean():\n{df_2_2.mean()}")
print(f"df_2_2.shape: {df_2_2.shape}")
print("-" * 50)

# ==================================================
# 실습 3 - 공정 센서 열 골라내기
print("\n=== 실습 3 - 공정 센서 열 골라내기 ===")
df_3 = pd.read_csv(
    "Data/13_diecasting_shot.csv",
    sep=",",
    encoding="utf-8",
)


# ==================================================
# 실습 4 - loc, iloc 행 선택하기
print("\n=== 실습 4 - loc, iloc 행 선택하기 ===")
df_4 = pd.read_csv(
    "Data/13_diecasting_shot.csv",
    sep=",",
    encoding="utf-8",
)

print(df_4.loc[0:2])
print(df_4.iloc[0:2])

print(len(df_4.loc[0:2]))  # 0~2 => 3
print(len(df_4.iloc[0:2]))  # 0~1 => 2

# loc로 라벨 기준 단일 행 선택
print(df_4.loc[0, "품질등급"])  # 양품

# iloc로 번호 기준 단일 행 선택
print(df_4.iloc[0]["품질등급"])  # 양품

# ==================================================
# 실습 5 - loc, iloc 행/열 동시 선택하기
print("\n=== 실습 5 - loc, iloc 행/열 동시 선택하기 ===")
df_5 = pd.read_csv(
    "Data/13_diecasting_shot.csv",
    sep=",",
    encoding="utf-8",
)

print(df_5.loc[0:3, ["주조압력", "사이클타임"]])


# ==================================================
# 실습 6 - 특정 구간 추출 종합
print("\n=== 실습 6 - 특정 구간 추출 종합 ===")
df_6 = pd.read_csv(
    "Data/13_diecasting_shot.csv",
    sep=",",
    encoding="utf-8",
)
cols = list(df_6.columns)
print(cols)
print("-" * 50)
print(f"df_6 [10,5] 뽑기 - 원래 데이터:\n{df_6.loc[10]}")
print(f"cols[5]: {cols[5]} | {df_6.loc[10, cols[5]]}")
print("-" * 50)
print(f"df_6 [11,2] 뽑기 - 원래 데이터:\n{df_6.loc[11]}")
print(f"cols[2]: {cols[2]} | {df_6.loc[11, cols[2]]}")
print("-" * 50)
print(f"df_6 [10,6] 뽑기 - 원래 데이터:\n{df_6.loc[10]}")
print(f"cols[2]: {cols[6]} | {df_6.loc[10, cols[6]]}")
print("-" * 50)
