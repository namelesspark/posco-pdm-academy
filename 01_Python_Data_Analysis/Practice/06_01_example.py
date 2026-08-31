print("\n===실습 1 - 센서를 튜플로 묶고 꺼내기 ===")

sensor = ("모터 온도", 78)
print(sensor[0], sensor[1], sep="\n")

name, val = sensor
print(name, val)


print("\n=== 실습 2 - 튜플 리스트를 반복 처리하기 ===")

effector = (
    "strymon",
    "Bigsky MX",
    36,
    127,
)

brand, name, decay, parameter = effector

for parameter in (parameter,):
    if parameter >= 90:
        print("parameter 값 큼", parameter)

print("\n=== 실습 3 - 중첩 튜플로 센서 위치 관리하기 ===")
val = [
    ("Reverb Decay", 72, (0, 100)),
    ("Wet Mix", 45, (0, 100)),
    ("Pre-delay", 28, (0, 200)),
]

for name, presence, bound in val:
    min_v, max_v = bound
    print(name, "최소 최대:", min_v, max_v)

for name, presence, bound in val:
    if presence > 50:
        print("50 초과 effector 값: ", name)


print("\n=== 실습 4 - 셋으로 중복 센서 제거하기 ===")
import random

ids = [f"WOR_{random.randint(1,10):02d}" for _ in range(10)]
print(ids)
unique = sorted(set(ids))
print("종류 개수: ", unique)


print("\n=== 실습 5 - 두 라인의 센서 구성 비교하기 ===")
anomaly_1 = {f"WOR_{random.randint(1,10):02d}" for _ in range(7)}
anomaly_2 = {f"WOR_{random.randint(1,10):02d}" for _ in range(7)}

union_anomaly = anomaly_1.union(anomaly_2)
inter_anomaly = anomaly_1.intersection(anomaly_2)
differ_1 = anomaly_1.difference(anomaly_2)
differ_2 = anomaly_2.difference(anomaly_1)
print("anomaly_1:", anomaly_1)
print("anomaly_2:", anomaly_2)
print("Union:", union_anomaly)
print("Intersection:", inter_anomaly)
print("Only anomaly_1:", differ_1)
print("Only anomaly_2:", differ_2)


print("\n=== 실습 6 - 두 시점의 이벤트 센서 추적하기 ===")
yesterday = {f"WOR_{random.randint(1,10):02d}" for _ in range(7)}
today = {f"WOR_{random.randint(1,10):02d}" for _ in range(7)}
print(f"어제: {yesterday}\n오늘: {today}")
print(f"신규 이상: {today.difference(yesterday)}")
print(f"지속 이상: {today.intersection(yesterday)}")
