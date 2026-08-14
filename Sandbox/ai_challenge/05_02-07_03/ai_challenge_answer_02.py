raw = [23.1, 24.5, 999.0, 25.2, 24.8, -50.0, 26.1, 27.3, 25.9, 28.4, 26.7, 31.9]
LOW, HIGH = -10.0, 100.0
WINDOW = 3

print("=" * 46)
print("      센서 노이즈 제거와 이동평균")
print("=" * 46)

clean = []
removed = []
for v in raw:
    if LOW <= v <= HIGH:
        clean.append(v)
    else:
        removed.append(v)

rate = len(removed) / len(raw) * 100
print(f"원본 {len(raw)}개 / 정상 {len(clean)}개 / 제거 {len(removed)}개")
print(f"제거된 값: {removed}")
print(f"제거율: {round(rate, 1)}%")

print("-" * 46)
moving = []
for i in range(len(clean) - WINDOW + 1):
    part = clean[i:i + WINDOW]
    moving.append(round(sum(part) / WINDOW, 2))

print(f"이동평균({WINDOW}구간) {len(moving)}개")
for idx, m in enumerate(moving, start=1):
    print(f"  {idx}. {m}")

print("-" * 46)
print("급변 구간:")
found = False
for i in range(len(moving) - 1):
    diff = moving[i + 1] - moving[i]
    if diff < 0:
        diff = -diff
    if diff > 1.0:
        print(f"  {i + 1}->{i + 2} 구간 급변 (차이 {round(diff, 2)})")
        found = True
if not found:
    print("  없음")

print("-" * 46)
print(f"정상값 평균: {round(sum(clean) / len(clean), 2)}")
print(f"최대: {max(clean)} / 최소: {min(clean)}")
print("=" * 46)
