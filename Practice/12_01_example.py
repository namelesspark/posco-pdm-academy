# ===========================================================
# 실습 1 - CSV 불러오기 워밍업
print("=== 실습 1. CSV 불러오기 워밍업 ===")
import pandas as pd
import os


import pandas as pd
import os

file_path = os.path.join("Data", "12_metro_small.csv")

try:
    df = pd.read_csv(file_path)
    print(df.shape)  # (30, 7)

    print(df.head(2))
except FileNotFoundError:
    print(f"파일이 없습니다 : {file_path}")


# ===========================================================
# 실습 2 - 설비 센서 CSV 불러오기
print("\n=== 실습 2 - 설비 센서 CSV 불러오기 ===")
try:
    file_path2 = os.path.join("Data", "12_metro_compressor.csv")
    df = pd.read_csv(file_path2)
    print(f"head로 확인\n{df.head(10)}")
except FileNotFoundError:
    print("파일 없음", file_path2)

# ===========================================================
# 실습 3 - 한글 / 구분자 깨짐 옵션 다루기
print("\n=== 실습 3 - 한글 / 구분자 깨짐 옵션 다루기 ===")
file_path3 = os.path.join("Data", "12_metro_small.csv")
try:
    df = pd.read_csv(
        file_path3,
        encoding="utf-8",
        sep=",",
        index_col="측정시각",
        nrows=5,
        usecols=["측정시각", "가동상태"],  # uscols=["가동상태"] : ValueError
    )
    print(df.shape)  # (30, 7)

    print(df.head(10))
except FileNotFoundError:
    print(f"파일이 없습니다 : {file_path3}")

# ===========================================================
# 실습 4 - 필요한 열만 골라 불러오기
print("\n=== 실습 4 - 필요한 열만 골라 불러오기 ===")
import pandas as pd

df = pd.read_csv(
    "data/12_metro_compressor.csv",
    usecols=["측정시각", "오일온도", "모터전류", "가동상태"],
)
print(df.shape)  # (200, 7) -> (200, 4)
print(df.head(3))


# ===========================================================
# 실습 5 - 경로 / 옵션 오류 고치기
print("\n=== 실습 5 - 경로 / 옵션 오류 고치기 ===")
import pandas as pd

file_path5 = os.path.join("Data", "잘못된파일이름.csv")

try:
    df = pd.read_csv(file_path5, encoding="utf-8")  # FileNotFoundError
    print("파일 읽기 성공!")
except FileNotFoundError:
    print("[오류 발생] 잘못된 파일 경로:", file_path5)
finally:
    print("올바른 경로 파일 shape")

    correct_path = "Data/12_metro_compressor.csv"
    if os.path.exists(correct_path):
        df_correct = pd.read_csv(correct_path, encoding="utf-8")
        print("올바른 경로 파일 shape:", df_correct.shape)
    else:
        print(f"({correct_path})도 없음")


# ===========================================================
# 실습 6 - read_csv 옵션 종합 연습
print("\n=== 실습 6 - read_csv 옵션 종합 연습 ===")
import csv

file_path6 = os.path.join("Data", "12_metro_compressor_semicolon.csv")
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print(next(reader))

try:
    df = pd.read_csv(
        file_path6,
        sep=";",
        encoding="utf-8",
        usecols=["측정시각", "오일온도", "모터전류"],
    )
    print(f"df shape: {df.shape}")
    print(df)

except FileNotFoundError:
    print(f"경로 없음 {file_path6}")
