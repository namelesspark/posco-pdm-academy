# 센서 csv를 안전하게 열어 헤더와 데이터를 분리한다.
# 파일이 없어도 멈추지 않게 FileNotFoundError에 대비한다.

import os, sys, csv

sys.stdout.reconfigure(encoding="utf-8")

file_path = os.path.join("Data", "09_ict_inspection_dirty.csv")


# 실습 - 1단계 csv 읽기
def print_col(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            print(f"헤더: {header}")
            print("=" * 60)
            count = 0
            for row in reader:
                print(row)
                count += 1
            print("=" * 60)
            print(f"총 데이터 개수: {count}")

    except FileNotFoundError:
        print("print_col: 파일 경로 인식 불가")


# 실습 - 2단계 조건 분류
# 부품명(설비명)별로 데이터를 묶기
# rows를 직접 넘기면 파일을 다시 읽지 않고 그 rows로만 그룹핑
def group_by_part(file_path, rows=None):

    grouped = {}

    if rows is None:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

    for row in rows:
        part = row["부품명"]
        info = {
            k: v for k, v in row.items() if k != "부품명"
        }  # 바깥 키와 중복되니 제외

        if part not in grouped:  # 처음 보는 설비명이면
            grouped[part] = []  # 빈 리스트부터 만들고
        grouped[part].append(info)  # 거기에 행을 추가

    return grouped


# 실습 - 3단계 통계 함수
# rows(딕셔너리 리스트)에서 col 컬럼의 개수, 평균, 최소, 최대를 계산
# 숫자가 아닌 값은 건너뛰고, 유효한 값이 하나도 없으면 None을 반환해 0으로 나누는 오류를 막는다.
def calc_stat(rows, col):
    total = 0
    count = 0
    min_val = None
    max_val = None

    for row in rows:
        try:
            value = float(row[col])
        except (ValueError, TypeError, KeyError):
            continue

        total += value
        count += 1
        if min_val is None or value < min_val:  # 최솟값 계산
            min_val = value
        if max_val is None or value > max_val:  # 최댓값 계산
            max_val = value

    if count == 0:
        return None

    return count, total / count, min_val, max_val


def calc_statistic(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        header = reader.fieldnames

    for col in header:  # 컬럼 하나 선택
        result = calc_stat(rows, col)  # 위의 3단계 함수를 재사용
        if result is None:
            print(f"{col}: 숫자값 없음")
        else:
            count, avg, min_val, max_val = result
            print(
                f"{col}: 유효 데이터 {count}개 | 평균: {avg:.2f} | 최소: {min_val} | 최대: {max_val}"
            )


# 실습 - 4단계 불량 방어
# 측정값을 검사해 정상 행은 valid에, 불량 행은 (검사ID, 사유)로 bad에 담음
# - 숫자로 못 바꾸는 값 -> float() 변환 시 자동으로 ValueError 발생 -> except에서 처리
# - 상한/하한을 벗어난 값 -> 직접 raise로 만들어서 같은 except에서 함께 처리
def filter_valid(file_path):

    valid = []
    bad = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            check_id = row.get("검사ID", "?")
            try:
                value = float(row["측정값"])
                low = float(row["하한치"])
                high = float(row["상한치"])

                if value < low or value > high:
                    raise ValueError(
                        f"측정값 {value}이(가) 정상범위({low}~{high})를 벗어남"
                    )

                valid.append(row)

            except (ValueError, TypeError, KeyError) as e:
                bad.append((check_id, str(e)))
                continue

    return valid, bad


# 실습 - 5단계 리포트 저장
def save_report(file_path, output_path):
    valid, bad = filter_valid(file_path)  # 4단계 함수 재사용
    stat = calc_stat(valid, "측정값")  # 3단계 함수 재사용

    lines = []
    lines.append("=== ICT 검사 데이터 분석 리포트 ===")
    lines.append(
        f"전체 {len(valid) + len(bad)}행 · 정상 {len(valid)}개 · 불량 {len(bad)}개"
    )
    lines.append("-" * 40)

    if stat is None:
        lines.append("측정값: 유효한 숫자 데이터 없음")
    else:
        _, avg, min_val, max_val = stat
        lines.append(f"측정값 평균 — {avg:.2f}")
        lines.append(f"측정값 최고 — {max_val}")
        lines.append(f"측정값 최저 — {min_val}")

    lines.append("-" * 40)
    lines.append("[불량 목록]")
    if bad:
        for check_id, reason in bad:
            lines.append(f"검사ID {check_id}: {reason}")
    else:
        lines.append("불량 없음")

    with open(output_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"리포트 저장 완료: {output_path}")

    # 저장 후 다시 열어 내용 확인
    with open(output_path, "r", encoding="utf-8") as f:
        print(f.read())


# 실습 - 6단계 통계 검증
def verify_by_part(file_path):
    valid, _ = filter_valid(file_path)  # 4단계 함수 재사용
    grouped = group_by_part(file_path, rows=valid)  # 2단계 함수 재사용

    total_by_part = 0
    for part, rows in grouped.items():
        result = calc_stat(rows, "측정값")  # 3단계 함수 재사용
        if result is None:
            print(f"{part}: 유효 데이터 없음")
            continue
        count, avg, min_val, max_val = result
        total_by_part += count
        print(f"{part}: {count}개 | 평균 {avg:.2f} | 최소 {min_val} | 최대 {max_val}")

    print("-" * 40)
    print(f"부품별 개수 합계: {total_by_part}")
    print(f"전체 정상 개수: {len(valid)}")
    print(f"검증 결과: {total_by_part == len(valid)}")


# ===================== 실행부 =====================

print_col(file_path)
print("=" * 80)

grouped = group_by_part(file_path)
for part, rows in grouped.items():
    print(f"{part}: {len(rows)}개")
    print(rows)
    print("-" * 40)
print("=" * 80)

calc_statistic(file_path)
print("=" * 80)

valid, bad = filter_valid(file_path)
print(f"정상 {len(valid)}개 / 불량 {len(bad)}개")
for check_id, reason in bad:
    print(f"  - 검사ID {check_id}: {reason}")
print("=" * 80)

report_path = os.path.join("Data", "09_ict_inspection_report.txt")
save_report(file_path, report_path)
print("=" * 80)

verify_by_part(file_path)
