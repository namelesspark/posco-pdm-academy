import os, csv, numpy as np, pandas as pd

file_path = os.path.join("Data", "12_metro_small.csv")

try:
    df = pd.read_csv(file_path, sep=",", index_col="모터전류", encoding="utf-8")
except FileNotFoundError:
    print(f"file not found:{file_path}")

print(df.count(1))
print("-" * 50)
print(df.shape)

