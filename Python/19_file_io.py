# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드(r)로 utf-8 형식의 변환을 거쳐 읽기로 한다
# 가져온 정보(파인 접근 열쇠/참조값)를 f에 담는다
f = open("sample.txt", "r", encoding="utf-8")

print(type(f).__name__)  # 타입의 이름 : TextIOWrapper

# 텍스트파일 파일 한줄씩 문자열을 만들어 리스트만들기
lines = f.readlines()
print(lines)

f.close()  # 열었다면 언젠가는 꼭 닫아줍시다

# 만약 신경써서 파일 닫기(close) 해주기 귀찮다면
# with open ... as 문법을 쓰는 것도 좋다
with open("sample.txt", "r", encoding="utf-8") as f:
    # 앞으로 이렇게 들여쓰기 된 코드가 끝나면
    # 파일 접근을 닫습니다(close)

    # 텍스트파일 파일 한줄씩 문자열을 만들어 리스트만들기
    lines = f.readlines()

print(lines)

# 쓰기모드(write)로 파일을 새롭게 만들어보겠습니다
f = open("hello.txt", "w", encoding="utf-8")

# 파일 쓰기에 줄바꿈을 포함하려면 \n을 포함시킨다
f.write("안녕하세요\n")
# 파일 쓰기에 탭들여쓰기를 포함하려면 \t를 포함시킨다
f.write("\t반갑습니다\n")

f.close()

# 이어쓰기 모드(append)로 파일에 내용을 추가합시다
f = open("hello.txt", "a", encoding="utf-8")

f.write("맛점하세요\n")

f.close()


import os
import sys
import csv

csv_path = os.path.join("Data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 강제종료시키기
if not os.path.exists(csv_path):
    print("파일이 없습니다")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1) 전달

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) # 이제 csv 전문가에게 맡깁시다
    reader = csv.reader(f)

    for row in reader:
        print(row)  # 각 행(row)마다 리스트로 출력됨


import os
import sys
import csv

csv_path = os.path.join("Data", "result.csv")

with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])


import os
import sys
import csv

csv_path = os.path.join("Data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 강제종료시키기
if not os.path.exists(csv_path):
    print("파일이 없습니다")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1) 전달

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
    # DictReader는 첫줄은 컬럼 이름으로 판단하고
    # 각 row를 해당 컬럼이름들을 key로 하는 딕셔너리로 만들어준다
    reader = csv.DictReader(f)

    for row in reader:
        print(row["설비ID"], row.get("시각"))


import os
import sys
import csv

csv_path = os.path.join("Data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 강제종료시키기
if not os.path.exists(csv_path):
    print("파일이 없습니다")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1) 전달

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) # 이제 csv 전문가에게 맡깁시다
    reader = csv.reader(f)

    # DictReader가 아닌 그냥 reader를 사용한다면
    # 보통 csv파일의 첫줄인 헤더줄도 읽어버린다
    # reader에게 첫줄은 건너뛰라고 말하는 방법이 필요하다
    # next(reader)는 한줄 건너뛰고 reader가 반응하게 한다
    header = next(reader)
    # header는 따로 리스트로 챙겨진다
    # ['설비ID', '시각', '진동X', '진동Y', '전류', '상태']
    print(header)

    for row in reader:
        print(row[0])  # 각 행(row)마다 리스트로 출력됨
