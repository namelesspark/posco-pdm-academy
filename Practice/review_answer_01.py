sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]

num_normal = 0
num_warning = 0
num_danger = 0
total_temp = 0
peak_temp = 0
peak_name = ""
total_facility = len(sensors)
danger_list = []

print("=" * 50 + "\n" + "\t   설비 종합 모니터링 리포트" + "\n" + "=" * 50)

for idx, (name, temp, vib) in enumerate(sensors, start=1):
    if temp > 90 or vib > 5.0:
        print(f"{idx}. {name} | 온도 {temp}℃ | 진동 {vib}mm/s | 위험 🚨")
        num_danger += 1
        danger_list.append(name)

        if peak_temp < temp:
            peak_temp = temp
            peak_name = name

    elif temp >= 80 or vib >= 3.0:
        print(f"{idx}. {name} | 온도 {temp}℃ | 진동 {vib}mm/s | 주의 👀")
        num_warning += 1
    else:
        print(f"{idx}. {name} | 온도 {temp}℃ | 진동 {vib}mm/s | 정상 ✅")
        num_normal += 1

    total_temp += temp

print("-" * 50)


print(f"총 설비: {total_facility}대")
print(f"정상: {num_normal} / 주의: {num_warning} / 위험: {num_danger}")
print(f"이상 설비 비율: {((num_warning + num_danger) / total_facility*100):.1f}%")
print(f"평균 온도: {total_temp / len(sensors):.1f}℃")
print(f"최고 온도 설비: {peak_name} ({peak_temp}℃)")
print(f"위험 설비 목록: {danger_list}")
print("=" * 50)
