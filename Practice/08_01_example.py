print("\n=== 실습 1 - import 세 방식으로 모듈 가져오기 ===")
# import 모듈명으로 통째로 가져와 모듈명.기능()으로 사용
# from 모듈 import 기능으로 일부만 가져와 모듈명 없이 사용

import random

x = random.randint(0, 10)
print(f"import random 결과 x: {x}")
import random as rd

x = rd.randint(0, 10)
print(f"import random as rd 결과 x: {x}")
from random import randint

x = randint(0, 10)
print(f"from random import randint 결과 x: {x}")

print("-" * 80)

print("\n=== 실습 2 - 표준 라이브러리로 센서값 만들기 ===")
# random 모듈 임포트
import random, math

# randint로 무작위 센서값 만들어 출력
sens_val = [
    random.randint(1, 100) for _ in range(20)
]  # 리스트에 20개 1~100 랜덤값 넣기
print(f"sens_val 랜덤 20개 값: {sens_val}")

# math 모듈로 값 가공(제곱근)
for idx, val in enumerate(sens_val):
    sens_val[idx] = round(math.sqrt(val), 4)

# 다시 실행하면 값이 달라지는지 확인
print(f"센서값 리스트 재출력 결과: {sens_val}")

print("-" * 80)

print("\n=== 실습 4 - os로 파일 존재 확인하기 ===")
# os를 import
import os

path_tuple = (
    os.path.join("Remind", "함수.pdf"),
    os.path.join("Remind", "함성.pdf"),
)  # path.join으로 폴더와 폴더 파일 이름을 이어 경로 만들기


def find_path(path):
    for p in path:
        print(
            f"{p} | 경로 참, 거짓 확인: {bool(os.path.exists(p))}"
        )  # path.exists로 그 경로가 있는지 참, 거짓 확인


print(f"파일 경로 튜플: {path_tuple}")
find_path(path_tuple)
print("-" * 80)

print("\n=== 실습 5 - datetime으로 점검 기록 남기기 ===")
# os와 datetime을 import
import os, datetime

# listdir로 폴더 파일 수 구하기
num_dir = len(os.listdir())

# datetime.now로 현재 시각을 담기
now = datetime.datetime.now()

# f-string으로 파일 수와 시각을 한 문장으로 출력
print(f"파일 수: {num_dir} | 현재 시각: {now}")


print("-" * 80)
print("\n=== 실습 3 - os로 폴더 목록 살펴보기 ===")
# 1 os 모듈 import
import os

# getcwd로 현재 작업 폴더 확인
print(f"현재 작업 폴더 확인: {os.getcwd()}")

# listdir로 폴더 안 목록을 변수에 담기
ls = [os.listdir()]
print("폴더 목록 리스트:", ls)


def find_csv_recursive(directory):

    try:
        items = os.listdir(directory)
    except PermissionError:
        return

    for item in items:  # for로 목록을 하나씩 출력하고 csv만 골라 출력
        full_path = os.path.join(directory, item)

        if os.path.isdir(full_path):
            find_csv_recursive(full_path)
        elif os.path.isfile(full_path) and item.endswith(".csv"):
            print(f"csv 파일 발견: {full_path}")


find_csv_recursive(os.getcwd())


print("-" * 80)
print("\n=== 실습 6 - 폴더에서 csv 파일만 골라내기 ===")
# os를 import하고 listdir로 폴더 목록을 구하기
import os

dir_list = []


def find_csv(directory):
    items = os.listdir(directory)

    for item in items:
        full_path = os.path.join(
            directory, item
        )  # 모은 csv마다 path.join으로 전체 경로를 만들기

        if os.path.isdir(full_path):
            find_csv(full_path)
        elif os.path.isfile(full_path) and item.endswith(
            ".csv"
        ):  # for-if로 .csv로 끝나는 이름만 빈 리스트에 모으기
            dir_list.append(full_path)


find_csv(os.getcwd())

for l in dir_list:
    print(f"csv 파일 디렉토리: {l}")
