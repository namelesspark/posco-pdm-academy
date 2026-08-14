production = [120, 0, 95, 130, -5, 110, 88, 0, 140, 102, 97, 115]
TARGET = 800

total = 0
i = 0
valid_count = 0
skipped = 0
reached = False

print("=" * 46)
print("      생산 목표 도달 시뮬레이션")
print("=" * 46)

while i < len(production):
    value = production[i]
    i += 1                      # continue 보다 위 -> 무한루프 방지

    if value <= 0:
        skipped += 1
        continue

    total += value
    valid_count += 1
    print(f"{i}회차: +{value} (누적 {total})")

    if total >= TARGET:
        reached = True
        break

print("-" * 46)
if reached:
    print(f"목표 달성! {i}회차에서 누적 {total}개 (목표 {TARGET})")
else:
    print(f"목표 미달: 누적 {total}개 / 목표 {TARGET}개")

print(f"유효 {valid_count}회 / 건너뜀 {skipped}회")
print("=" * 46)
