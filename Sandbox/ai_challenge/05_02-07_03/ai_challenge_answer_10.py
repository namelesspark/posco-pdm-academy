def clean_values(values, low, high):
    """범위(low~high) 안의 값만 담은 새 리스트를 돌려준다."""
    result = []
    for v in values:
        if low <= v <= high:
            result.append(v)
    return result


def get_stats(values):
    """(평균, 최소, 최대) 세 값을 돌려준다. 빈 리스트면 (0, 0, 0)."""
    if len(values) == 0:
        return 0, 0, 0
    return sum(values) / len(values), min(values), max(values)


def judge(avg, danger=90):
    """평균이 danger 이상이면 위험, 아니면 정상."""
    if avg >= danger:
        return "위험"
    return "정상"


plant = {
    "압축기_A": [78, 85, 999, 88, 82],
    "펌프_B":   [95, 97, 99, 101, 98],
    "송풍기_C": [55, 54, -20, 56, 58],
    "절단기_D": [88, 91, 89, 90, 92],
    "성형기_E": [70, 68, 72, 71, 69],
}
yesterday_alerts = {"펌프_B", "성형기_E"}
VALID_LOW, VALID_HIGH = 0, 200
DANGER = 90

print("=" * 58)
print("          스마트 정비 통합 리포트")
print("=" * 58)

today_alerts = set()
ranking = []
normal_count = 0
danger_count = 0

for name, raw in plant.items():
    clean = clean_values(raw, VALID_LOW, VALID_HIGH)
    removed = len(raw) - len(clean)
    avg, low, high = get_stats(clean)
    verdict = judge(avg, danger=DANGER)

    print(f"{name}")
    print(f"   원본 {len(raw)}개 / 정제 {len(clean)}개 (이상치 {removed}개 제거)")
    print(f"   평균 {round(avg, 2)} / 최소 {low} / 최대 {high} -> {verdict}")

    ranking.append((avg, name))

    if verdict == "위험":
        today_alerts.add(name)
        danger_count += 1
    else:
        normal_count += 1

print("-" * 58)
print(f"오늘 이상 설비: {sorted(today_alerts)}")
print(f"어제 이상 설비: {sorted(yesterday_alerts)}")
print(f"  신규 이상: {sorted(today_alerts - yesterday_alerts)}")
print(f"  지속 이상: {sorted(today_alerts & yesterday_alerts)}")
print(f"  해소된 설비: {sorted(yesterday_alerts - today_alerts)}")

print("-" * 58)
ranking.sort(reverse=True)
print("평균 상위 3개:")
i = 0
while i < 3 and i < len(ranking):
    avg, name = ranking[i]
    print(f"  {i + 1}위: {name} - {round(avg, 2)}")
    i += 1

print("-" * 58)
total = len(plant)
rate = danger_count / total * 100
print(f"전체 {total}대 / 정상 {normal_count}대 / 위험 {danger_count}대")
print(f"위험 비율: {round(rate, 1)}%")
print("=" * 58)
