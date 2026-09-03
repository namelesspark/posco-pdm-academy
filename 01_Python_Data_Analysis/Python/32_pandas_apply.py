import pandas as pd

df = pd.DataFrame({"점수": [60, 70, 80, 90]})

print(df)


def isPass(row, name, temp):
    if row["점수"] >= 60:
        return name + "합격" + temp
    else:
        return "불합격"


# apply() DataFrame의 모든 행, 열 기준으로 함수를 적용할 수 있도록 하는 메서드
# - apply() 인자: apply(func, axis=>0아니면1, ... 함수의 나머지 인자)

df["결과"] = df.apply(isPass, axis=1, name="allie", temp="~")  # 모든 행의 결과물 계산

print(df)
