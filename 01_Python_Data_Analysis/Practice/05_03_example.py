print("\n=== 실습 1 - 조건에 맞는 값만 출력하기 ===")
import random

count = random.randint(5, 10)
temps = [round(random.uniform(-10, 40), 1) for _ in range(count)]
print(temps)
for i in range(count):
    if temps[i] >= 30:
        print(f"고온: {temps[i]}")

print("\n=== 실습 2 - 두 조건을 모두 만족하는 값 고르기 ===")
import random

count = random.randint(5, 10)
time_list = [round(random.randint(1, 10), 1) for _ in range(count)]
print(f"가동시간 리스트: {time_list}")

fit_time = []
for t in time_list:
    if 5 <= t <= 10:
        fit_time.append(t)

print(f"조건을 만족하는 가동 시간 리스트: {fit_time}")


print("\n=== 실습 3 - 조건에 맞는 값만 골라 평균 구하기 ===")
import random

count = random.randint(5, 10)
t_list = [round(random.uniform(20, 40), 1) for _ in range(count)]

total = 0
num = 0
idx_list = []
for idx, t in enumerate(t_list):
    if t > 30:
        total += t
        idx_list.append(idx)
print(f"온도 리스트: {t_list}")
print(f"30 초과 온도의 합: {total}")
print(f"30 초과 온도 인덱스: {idx_list}")
print(f"30 초과 온도 개수: {len(idx_list)}")

if idx_list:
    print(f"고온 평균: {total / len(idx_list):.1f}")
else:
    print("고온 평균: 30 초과 데이터 없음")


print("\n=== 실습 4 - 조건에 맞는 값으로 새 리스트 만들기 ===")
count = random.randint(5, 10)
t_list = [round(random.uniform(20, 40), 2) for _ in range(count)]
print(f"온도 리스트: {t_list}")

hot = []
for idx, t in enumerate(t_list):
    if t > 30:
        hot.append(t)
print(f"30 초과 리스트: {hot}", f"개수: {len(hot)}", sep=" / ")


print("\n=== 실습 5 - 값을 가공해 새 리스트 만들기 ===")

count = random.randint(5, 10)
celsius = [round(random.uniform(20, 40), 2) for _ in range(count)]

fahrenheit = []

for c in celsius:
    fahrenheit.append(round((c * 1.8 + 32), 1))
print(f"섭씨 리스트: {celsius} \n화씨 변환 리스트: {fahrenheit}", sep=" / ")


print("\n=== 실습 6 - 센서 데이터 종합 분석하기 ===")

count = random.randint(10, 20)
celsius = [round(random.uniform(20, 40), 2) for _ in range(count)]

total = 0
l = []
for c in celsius:
    total += c

    if c > 30:
        l.append(c)

print(
    f"온도 리스트: {celsius}\n전체 평균: {(total / count):.2f}\n고온 개수: {len(l)}\n고온 평균: {(sum(l) / len(l)):.2f}"
)
