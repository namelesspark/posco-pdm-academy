sensors = {"모터온도": 78, "진동": 0.5, "펌프압력": 95, "유량": 42}
new_data = {"모터온도": 82, "전류": 61, "진동": 0.8}
broken = "유량"
query_list = ["모터온도", "회전속도", "전류", "습도"]

print("=" * 50)
print("        센서 카탈로그 관리 시스템")
print("=" * 50)

print(f"등록 센서 {len(sensors)}개")
print(f"키 목록: {list(sensors.keys())}")
print(f"값 목록: {list(sensors.values())}")

print("-" * 50)
updated = []
added = []
for key in new_data:
    if key in sensors:
        updated.append(key)
    else:
        added.append(key)

sensors.update(new_data)
print(f"갱신된 센서: {sorted(updated)}")
print(f"추가된 센서: {sorted(added)}")
print(f"반영 후 {len(sensors)}개")

print("-" * 50)
if broken in sensors:
    del sensors[broken]
    print(f"고장 센서 '{broken}' 삭제 -> 남은 {len(sensors)}개")
else:
    print(f"'{broken}' 은 등록되지 않은 센서")

print("-" * 50)
print("조회 결과:")
for q in query_list:
    value = sensors.get(q)
    if value is None:
        print(f"  {q}: 미등록")
    else:
        print(f"  {q}: {value}")

print("-" * 50)
high = []
for name, value in sensors.items():
    if value >= 60:
        high.append((value, name))

high.sort(reverse=True)
print("60 이상 센서(내림차순):")
for value, name in high:
    print(f"  {name} = {value}")

print("-" * 50)
total = sum(sensors.values())
print(f"합계 {total} / 평균 {round(total / len(sensors), 2)}")
print("=" * 50)
