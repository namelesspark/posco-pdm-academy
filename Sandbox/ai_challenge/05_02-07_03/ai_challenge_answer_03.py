sensors = [
    ("압축기_A", (3.0, 4.0), 62),
    ("펌프_B",   (1.5, 2.0), 71),
    ("송풍기_C", (6.0, 8.0), 55),
    ("절단기_D", (0.9, 1.2), 88),
    ("성형기_E", (5.0, 12.0), 47),
]

print("=" * 52)
print("         합성진동 기준 설비 랭킹")
print("=" * 52)

ranking = []
double_risk = []

for name, vib, current in sensors:
    x, y = vib
    combined = (x ** 2 + y ** 2) ** 0.5
    print(f"{name} | X {x} | Y {y} | 합성 {round(combined, 2)} | 전류 {current}A")

    ranking.append((combined, name))

    if combined >= 5.0 and current >= 60:
        double_risk.append(name)

print("-" * 52)
ranking.sort(reverse=True)

print("합성진동 순위:")
for rank, (score, name) in enumerate(ranking, start=1):
    print(f"  {rank}위: {name} - {round(score, 2)}")

print("-" * 52)
top_score, top_name = ranking[0]
print(f"최고 진동 설비: {top_name} ({round(top_score, 2)})")

double_risk.sort()
print(f"이중위험(합성>=5.0 & 전류>=60): {double_risk}")
print("=" * 52)
