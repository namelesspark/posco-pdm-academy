import pandas as pd
import os

###############################################################################
# 8/18 종합 실습 Pandas - groupby
###############################################################################
path_advanced = os.path.join("data", "students_groupby_practice.csv")
df_advanced = pd.read_csv(path_advanced, encoding="utf-8")

print(df_advanced.info())
print(df_advanced.head())

# 문제 1 - 이 학교의 전체 학생 수를 구하세요.
print("-" * 100, "\n", "전체 학생 수: ", len(df_advanced))

# 문제 2 - 학년 별 학생 수를 구하세요.
print("-" * 100, "\n", "학년 별 학생 수:")
print(df_advanced.groupby("학년").size())

# 문제 3 - 학년 내 각 반별 학생 수를 구하세요.
for (grade, classroom), group in df_advanced.groupby(["학년", "반"]):
    print(f"{grade}학년 {classroom}반 학생 수: {len(group)}명")

# 문제 4 - 각 반(학년, 반 포함)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
for (grade, classroom), group in df_advanced.groupby(["학년", "반"]):
    kor_mean = round(group["국어"].mean(), 2)
    print(f"{grade}학년 {classroom}반 국어 평균: {kor_mean}점")

# 문제 5 - 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.
for (grade, classroom), group in df_advanced.groupby(["학년", "반"]):
    eng_mean = round(group["영어"].mean(), 2)
    print(f"{grade}학년 {classroom}반 영어 평균: {eng_mean}점")
