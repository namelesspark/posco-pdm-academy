def get_average(values):
    """숫자 리스트를 받아 평균을 돌려준다. 빈 리스트면 0."""
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def get_min_max(values):
    """숫자 리스트를 받아 (최솟값, 최댓값) 튜플을 돌려준다. 빈 리스트면 (0, 0)."""
    if len(values) == 0:
        return 0, 0
    return min(values), max(values)


def count_over(values, limit):
    """limit 을 초과하는 값의 개수를 돌려준다."""
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count


def judge(avg):
    """평균값을 받아 위험/주의/정상 판정 문자열을 돌려준다."""
    if avg >= 90:
        return "위험"
    elif avg >= 80:
        return "주의"
    return "정상"


line_a = [78, 85, 92, 66, 88, 74]
line_b = [95, 97, 99, 101]
line_c = []

lines = [("A라인", line_a), ("B라인", line_b), ("C라인", line_c)]

print("=" * 52)
print("         센서 통계 함수 세트")
print("=" * 52)

for name, data in lines:
    avg = get_average(data)
    low, high = get_min_max(data)
    over = count_over(data, 90)
    verdict = judge(avg)

    print(f"[{name}] 측정 {len(data)}회")
    print(f"   평균 {round(avg, 2)} / 최소 {low} / 최대 {high}")
    print(f"   90 초과 {over}개 -> 판정: {verdict}")

print("=" * 52)
