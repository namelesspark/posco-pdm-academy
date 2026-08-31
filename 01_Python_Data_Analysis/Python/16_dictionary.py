data_class_list = [
    "태구",
    "수진",
    "영준",
    "민지",
    "현우",
    "지훈",
    "하늘",
    "서연",
    "민석",
    "지우",
]


# 딕셔너리는 역할까지 부여할 수 있는 자료구조이다
data_class_dict = {
    "반장": "태구",
    "부반장": "수진",
    "총무": "영준",
    "서기": "민지",
    "회계": "현우",
}

# 센서로부터 얻는 예시 데이터로 딕셔너리를 만들어봅시다
# 설비 고장 예측을 위한 센서 데이터 예시 (정상 및 고장 징후 데이터 반영)
sensors_list = [
    {"센서 이름": "motor_vibration", "진동": 4.8, "온도": 78.5},
    {"센서 이름": "pump_pressure", "압력": 2.1, "유량": 45.2},
    {"센서 이름": "compressor_temp", "온도": 92.4, "진동": 1.8},
    {"센서 이름": "bearing_vibe", "진동": 8.2, "속도": 1750},
    {"센서 이름": "fan_current", "전류": 24.5, "온도": 55.0},
    {"센서 이름": "gearbox_noise", "진동": 5.1, "소음": 88.5},
    {"센서 이름": "turbine_rpm", "회전수": 3590, "온도": 62.1},
    {"센서 이름": "hydraulic_oil", "압력": 12.4, "점도": 46.2},
    {"센서 이름": "generator_volt", "전압": 220.4, "전류": 15.1},
    # {"센서 이름": "conveyor_load", "하중": 450, "속도": 1.2},
]

print(type(sensors_list))
print(sensors_list[0])
sensors_list[0]["센서 이름"] = "motor_vib"
print(sensors_list[0])

# 필요없는 key와 그 value를 삭제


# ======================================================
s_dict = {"센서 이름": "conveyor_load", "하중": 450, "속도": 1.2}
print(s_dict.get("센서 이름"))

now_weight = s_dict.get("하중")  # 여기서 속도라는 1.2가 motor_degree에 나오는가?
next_weight = now_weight + 10
print(next_weight)
print(type(next_weight))


# 두 딕셔너리가 있을 때
# 실제 데이터
values = {"모터 온도": 95, "압력": 88, "진동": 4.5}
# 임계치 데이터
limits = {"모터 온도": 90, "압력": 90}
# 는 같은 key 값을 가지고 있다.

for name, value in values.items():
    print(f"{name} | {value}")

    if value > limits.get(name, 0):
        print("경고")


location_dict = {
    "시": [
        {"이름": "서울특별시", "기초단체": ["종로구", "동구", "마포구"]},
        {"이름": "대구광역시", "기초단체": ["중구", "수성구", "달서구"]},
    ],
    "도": [
        {"이름": "경기도", "기초단체": ["수원시", "안산시", "안양시"]},
        {"이름": "경상북도", "기초단체": ["포항시", "경주시", "김천시"]},
    ],
}

print(location_dict)
print("=" * 80)
print(location_dict["시"])
print("=" * 80)
print(location_dict.get("도"))
print("=" * 80)
print(location_dict["시"][0])
print("=" * 80)
print(location_dict["시"][1])
print("=" * 80)
print(location_dict.get("도")[1].get("이름"))

for basic_dict in location_dict.get("도"):
    print(basic_dict.get("이름"))
    print(basic_dict.get("기초단체"))

# 시와 도 단위 딕셔너리를 각각 출력하기
