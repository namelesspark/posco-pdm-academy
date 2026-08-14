names  = ["모터온도", "진동", "펌프압력", "전류", "유량"]
values = [95, 0.8, 88, 61, 47]

limits = {"모터온도": 90, "진동": 1.0, "펌프압력": 90, "전류": 50}

print("=" * 56)
print("        측정값 대 임계값 초과율 분석")
print("=" * 56)

measured = dict(zip(names, values))
print(f"측정 딕셔너리 {len(measured)}개: {measured}")

print("-" * 56)
over_list = []
rate_total = 0
rate_count = 0

for name, value in measured.items():
    limit = limits.get(name)

    if limit is None:
        print(f"{name}: 임계값 미등록 -> 판정 불가")
        continue

    rate = value / limit * 100
    rate_total += rate
    rate_count += 1

    if rate > 100:
        mark = "초과"
        over_list.append(name)
    elif rate >= 90:
        mark = "임박"
    else:
        mark = "정상"

    print(f"{name}: 측정 {value} / 임계 {limit} -> {round(rate, 1)}% [{mark}]")

print("-" * 56)
if over_list:
    over_list.sort()
    print(f"초과 센서: {over_list}")
else:
    print("초과 없음")

print(f"판정 대상 {rate_count}개 / 평균 초과율 {round(rate_total / rate_count, 2)}%")
print("=" * 56)
