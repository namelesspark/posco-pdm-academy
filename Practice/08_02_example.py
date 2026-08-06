# 실습 1
print("\n=== 실습 1 - open으로 파일 읽기 ===")
f = open("Data/08_press.csv", "r", encoding="utf-8")
print(f.readlines(5))

# with open("Data/08_press.csv", "r", encoding="utf-8") as f:
#     lines = f.readlines()
# print(type(lines).__name__, len(lines))
# print(lines)


# 실습 2
print("\n=== 실습 2 - with open으로 파일에 쓰기 ===")

with open("Data/sample.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(["123", "456"]))
    f.write("\n1\n")
    f.writelines(["1", "2", "3"])

with open("Data/sample.txt", "r", encoding="utf-8") as f:
    print(f.readlines())


# 실습 3
print("\n=== 실습 3 - a 모드로 기록 이어붙이기 ===")

with open("Data/sample.txt", "a", encoding="utf-8") as f:
    f.write("\na로 이어쓰기 시작")

f = open("Data/sample.txt", "r", encoding="utf-8")
print(f.read())

f.close()


# 실습 4
print("\n=== 실습 4 - csv.reader로 csv 읽기 ===")

import csv

with open("Data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 실습 5
print("\n=== 실습 5 - csv.writer로 csv 쓰기 ===")

import csv

with open("Data/08_press.csv", "a", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])


with open("Data/08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# 실습 6
print("\n=== 실습 6 - CSV 읽어 조건 저장하기 ===")

# csv를 import
import csv, os

# csv.reader로 읽고 첫 줄 헤더는 건너뛰기
csv_path = os.path.join("Data", "08_press.csv")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for idx, row in enumerate(reader):
        if idx == 0:
            continue

        data_range = row[1:-1]

        if len(data_range) > 0 and data_range[0] != "":
            print(data_range)
