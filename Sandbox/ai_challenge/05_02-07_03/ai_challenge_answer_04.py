morning   = {"S01", "S02", "S03", "S05", "S08"}
afternoon = {"S02", "S03", "S06", "S08"}
night     = {"S03", "S05", "S07", "S08"}

print("=" * 52)
print("        3교대 경고 센서 교차 분석")
print("=" * 52)

print(f"오전조 {len(morning)}종: {sorted(morning)}")
print(f"오후조 {len(afternoon)}종: {sorted(afternoon)}")
print(f"야간조 {len(night)}종: {sorted(night)}")

print("-" * 52)
all_three = morning & afternoon & night
total = morning | afternoon | night

print(f"전체 경고 센서 {len(total)}종: {sorted(total)}")
print(f"3개 조 전부(상시 이상): {sorted(all_three)}")

two_or_more = (morning & afternoon) | (afternoon & night) | (morning & night)
exactly_two = two_or_more - all_three
exactly_one = total - two_or_more

print(f"정확히 2개 조(간헐 이상): {sorted(exactly_two)}")
print(f"정확히 1개 조(단발 이상): {sorted(exactly_one)}")

print("-" * 52)
check = len(exactly_one) + len(exactly_two) + len(all_three)
print(f"분류 합계 {check}종 / 전체 {len(total)}종")
if check == len(total):
    print("검산 OK")
else:
    print("검산 실패")
print("=" * 52)
