# 학생들의 점수를 가져와서 각 학생별 합계 평균과
# 모든 학생들의 평균 점수를 내는 코드
import os, csv, sys

file_path = os.path.join("Data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾을 수 없음")
    sys.exit()

total = 0
students_count = 0
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", 0)
        kor = row.get("국어", -1)
        eng = row.get("영어", -1)
        math = row.get("수학", -1)

        student_avg = (int(kor) + int(eng) + int(math)) / 3
        total += student_avg
        students_count += 1
        print(f"{name} | {kor} | {eng} | {math} | 평균: {student_avg:.1f}")

print(f"전체 학생 수: {students_count}\n전체 평균: {round(total / students_count, 1)}")


## 제출 안하는 실습
# 위 코드를 기반으로 최고점 학생, 최저점 학생도 찾아서 출력해보기

import os, csv, sys

file_path = os.path.join("Data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾을 수 없음")
    sys.exit()

total = 0
students_count = 0
peak_kor, peak_kor_student = 0, ""
peak_eng, peak_eng_student = 0, ""
peak_math, peak_math_student = 0, ""

with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", 0)
        kor = int(row.get("국어", -1))
        eng = int(row.get("영어", -1))
        math = int(row.get("수학", -1))

        student_avg = (kor + eng + math) / 3
        total += student_avg
        students_count += 1
        print(f"{name} | {kor} | {eng} | {math} | 평균: {student_avg:.1f}")

        if peak_kor < kor:
            peak_kor = kor
            peak_kor_student = name
        if peak_eng < eng:
            peak_eng = eng
            peak_eng_student = name
        if peak_math < math:
            peak_math = math
            peak_math_student = name


print(f"전체 학생 수: {students_count}\n전체 평균: {round(total / students_count, 1)}")
print(f"국어 최고점: {peak_kor} | {peak_kor_student}")
print(f"영어 최고점: {peak_eng} | {peak_eng_student}")
print(f"수학 최고점: {peak_math} | {peak_math_student}")
