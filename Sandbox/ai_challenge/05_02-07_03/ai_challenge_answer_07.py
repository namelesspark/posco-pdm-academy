plant = {
    "1번모터": {"상태": "정상", "이력": [78, 79, 81, 80]},
    "2번펌프": {"상태": "경고", "이력": [92, 95, 97, 99, 101]},
    "3번팬":   {"상태": "정상", "이력": [55, 54, 56]},
    "4번압축기": {"상태": "경고", "이력": [88, 91]},
}

print("=" * 54)
print("          설비별 측정 이력 관리")
print("=" * 54)

warning_list = []
all_values = []
avg_rank = []

for name, info in plant.items():
    state = info["상태"]
    history = info["이력"]

    avg = sum(history) / len(history)
    trend = history[-1] - history[0]

    if trend > 0:
        trend_mark = "상승"
    elif trend < 0:
        trend_mark = "하락"
    else:
        trend_mark = "유지"

    print(f"{name} [{state}] 측정 {len(history)}회")
    print(f"   이력: {history}")
    print(f"   평균 {round(avg, 2)} / 최대 {max(history)} / 최소 {min(history)}")
    print(f"   추세: {trend_mark} ({trend:+d})")

    if state == "경고":
        warning_list.append(name)

    all_values.extend(history)
    avg_rank.append((avg, name))

print("-" * 54)
warning_list.sort()
print(f"경고 설비: {warning_list}")

print(f"전체 측정 {len(all_values)}회 / 전체 평균 {round(sum(all_values) / len(all_values), 2)}")

avg_rank.sort(reverse=True)
top_avg, top_name = avg_rank[0]
print(f"최고 평균 설비: {top_name} ({round(top_avg, 2)})")

print("-" * 54)
# 대괄호를 연달아 써서 3층(딕셔너리 -> 딕셔너리 -> 리스트)을 직접 뚫기
print(f'2번펌프 이력 첫 값: {plant["2번펌프"]["이력"][0]}')
print(f'2번펌프 이력 끝 값: {plant["2번펌프"]["이력"][-1]}')

target = "5번밸브"
if target not in plant:
    print(f"{target}: 미등록 설비")
print("=" * 54)
