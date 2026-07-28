print("=== 실습 1 - 나만의 데이터 리스트 만들기 ===")
measure_temps = [34, 35, 35, 34, 32, 30]
empty_list = []
print(
    f"{measure_temps}",
    f"{len(measure_temps)}",
    f"{empty_list}",
    f"{len(empty_list)}",
    sep=" / ",
)


print("\n=== 실습 2 - 인덱스로 값 꺼내기 ===")
measure_temps = [34, 35, 35, 34, 32, 30]
print(measure_temps[0], measure_temps[2], measure_temps[-1], sep=" / ")


print("\n=== 실습 3 - 인덱스로 꺼낸 값 계산하기 ===")
prod = [100, 110, 90, 125, 110, 90]
add_prod = prod[0] + prod[-1]
print(add_prod, add_prod / 2, sep=" / ")

print("\n=== 실습 4 - 슬라이싱으로 구간 자르기 ===")
temps = [20, 22, 28, 23, 25, 31, 22, 19, 23, 22]
print(f"{temps[:3]}", f"{temps[-3:]}", f"{len(temps[:3])}", sep=" / ")

print("\n=== 실습 5 - 데이터를 두 구간으로 나누기 ===")
data_list = [20, 22, 28, 23, 25, 31, 22, 19, 23, 22, 24, 27]  # 12개 값
first = data_list[:6]
second = data_list[-6:]
print(first, second, len(first), len(second), sep=" / ")


print("\n=== 실습 6 - 값 찾아 바꾸기 ===")
temps_list = [23, 26, 22, 240, 25, 22, 21, 20]
print(temps_list)
if 240 in temps_list:
    idx = temps_list.index(240)
    temps_list[idx] = 24
print(temps_list)

print("\n=== 실습 6 - 값 찾아 바꾸기 (최적화) ===")
temps_list = [23, 26, 22, 240, 25, 22, 21, 20]
print(temps_list)

try:
    idx = temps_list.index(240)
    temps_list[idx] = 24
except ValueError:
    pass

print(temps_list)


print("\n=== 실습 7 - 측정 값 추가하기 ===")
empty_list = []
empty_list.append(55), print(empty_list)
empty_list.insert(0, 92), print(empty_list)
empty_list.extend([100, 200, 300]), print(empty_list)
