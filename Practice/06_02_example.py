# 포켓몬 1, 2, 3 진화 단계를 딕셔너리로 만들고
# 포켓몬 딕셔너리들이 모인 배열을 만들어 봅시다
# 가능하면, 배열의 데이터를 for - in을 사용해서 하나씩 꺼내 print해보기
pkm_dict = [
    {"진화 1단계": "이상해씨", "진화 2단계": "이상해풀", "진화 3단계": "이상해꽃"},
    {"진화 1단계": "파이리", "진화 2단계": "리자드", "진화 3단계": "리자몽"},
    {"진화 1단계": "꼬부기", "진화 2단계": "어니부기", "진화 3단계": "거북왕"},
    {"진화 1단계": "캐터피", "진화 2단계": "단데기", "진화 3단계": "버터풀"},
    {"진화 1단계": "뿔충이", "진화 2단계": "딱충이", "진화 3단계": "독침붕"},
    {"진화 1단계": "구구", "진화 2단계": "피죤", "진화 3단계": "피죤투"},
    {"진화 1단계": "피츄", "진화 2단계": "피카츄", "진화 3단계": "라이츄"},
    {"진화 1단계": "미뇽", "진화 2단계": "신뇽", "진화 3단계": "망나뇽"},
    {"진화 1단계": "니드런", "진화 2단계": "니드리노", "진화 3단계": "니드킹"},
    {"진화 1단계": "푸푸린", "진화 2단계": "푸린", "진화 3단계": "푸크린"},
]
print("=" * 80)
print("\t\t\t\t포켓몬 진화 3단계 출력")
print("=" * 80)
for d in pkm_dict:
    print(d)
    for key, val in d.items():  # 가져온 딕셔너리의 key, value를 꺼내기
        print(f"{key} | {val}")
print("=" * 80)


print("=== 실습 1 - 딕셔너리 만들고 다루기 ===")
# 1. 센서 명을 키, 측정값을 값으로 딕셔너리 저장
# 2. 키로 값을 꺼내고 새 키로 추가 / 기존 키로 수정
# 3. get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
sensors_dict = {"센서명": "compressor_temp", "온도": 92.4, "진동": 1.8}  # 1번
print("키 조회 결과:", sensors_dict.get("온도"))  # 2번 키로 값 출력
sensors_dict["압력"] = 2.1  # 2번 새 키 추가
print("압력 추가 결과 - 압력값:", sensors_dict["압력"])
print(
    "get으로 없는 키 조회(유량):", sensors_dict.get("유량", 0)
)  # 없는 키 조회(0 기본값)
print("in으로 키 존재 확인(진동):", "진동" in sensors_dict)
print("in으로 키 존재 확인(회전수):", "회전수" in sensors_dict)

print("-" * 70)


print("\n=== 실습 2 - update로 여러 값 한 번에 갱신하기 ===")
# ①센서 딕셔너리와 새 데이터 딕셔너리를 각각 저장
# ②update로 새 데이터를 한 번에 반영(있으면 수정, 없으면 추가)
# ③del로 특정 키를 삭제하고 len으로 개수 확인
sensor_dict = {"센서 이름": "generator_volt", "전압": 220.4, "전류": 15.1}
new_data = {"센서 이름": "hydraulic_oil", "압력": 12.4, "점도": 46.2}
print(f"센서 딕셔너리: {sensor_dict}")
sensor_dict.update(new_data)
print(f"new_data update: {sensor_dict}")

print("-" * 70)


print("\n=== 실습 3 - 딕셔너리로 통계 내기 ===")
# ①센서명-측정값 딕셔너리 저장
# ②values의 합을 개수로 나눠 평균 구하기
# ③items로 순회하며 가장 큰 값과 그 센서명을 찾아 출력
sensor_data = {
    "VIB_SENSOR_01": 4.8,
    "VIB_SENSOR_02": 78.5,
    "VIB_SENSOR_03": 2.1,
    "VIB_SENSOR_04": 45.2,
    "VIB_SENSOR_05": 92.4,
    "VIB_SENSOR_06": 1.8,
    "VIB_SENSOR_07": 8.2,
    "VIB_SENSOR_08": 55.0,
    "VIB_SENSOR_09": 5.1,
    "VIB_SENSOR_10": 88.5,
}
total = 0  # 측정 값 전체
top_val = 0  # 가장 큰 값
top_val_name = 0  # 가장 큰 값을 가지는 key

for name, value in sensor_data.items():  # items 순환
    total += value
    if top_val < value:
        top_val = value
        top_val_name = name

print(f"센서값 평균: {round(total / len(sensor_data), 1)}")
print(f"가장 큰 값({top_val_name}): {top_val}")

print("-" * 70)


print("\n=== 실습 4 - zip으로 센서명-값 매핑하기 ===")
# ①센서명 리스트와 측정값 리스트를 각각 저장
# ②zip으로 두 리스트를 짝지어 dict로 변환
# ③items로 순회하며 이름-값 쌍 출력
sensor_name = ["온도", "진동", "압력"]
sensor_val = [92.4, 4.8, 12.4]
sensors = dict(zip(sensor_name, sensor_val))
print(f"센서명 리스트: {sensor_name}")
print(f"센서값 리스트: {sensor_val}")
print(f"zip 결과: {sensors}")
print("-" * 70)


print("\n=== 실습 5 - 임계값으로 경고 센서 분류하기 ===")
# ①측정값 딕셔너리와 임계값 딕셔너리를 각각 저장
# ②items로 순회하며 각 센서 값이 같은 이름의 임계값을 넘는지 비교
# ③넘는 센서 이름을 빈 리스트에 모아 출력
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
    {"센서 이름": "conveyor_load", "하중": 450, "속도": 1.2},
]

limits = {
    "진동": 5.0,
    "온도": 80.0,
    "압력": 10.0,
    "유량": 50.0,
    "속도": 1500,
    "전류": 20.0,
    "소음": 85.0,
    "회전수": 3500,
    "점도": 45.0,
    "전압": 230.0,
    "하중": 400,
}

warning = []
for sensor in sensors_list:
    name = sensor["센서 이름"]
    for key, value in sensor.items():
        if key == "센서 이름":
            continue
        elif key in limits and value > limits[key]:
            warning.append(name)
print(f"임계값:", limits)
print(f"초과 리스트:", warning)
print("-" * 70)


print("\n=== 실습 6 - 중첩 딕셔너리로 설비 관리하기 ===")
# ①설비명을 키로, 각 설비 정보(딕셔너리)를 값으로 하는 중첩 딕셔너리 저장
factory_equipment = {
    "Compressor_A": {"status": "정상", "temperature": 42.5, "pressure": 3.2},
    "Pump_B": {"status": "경고", "temperature": 68.1, "pressure": 1.8},
    "Motor_C": {"status": "정상", "temperature": 35.4, "vibration": 2.5},
}

# ②중첩 키로 특정 설비의 특정 값을 꺼내기
print("Pump_B의 온도:", factory_equipment["Pump_B"]["temperature"])

# ③items 순회로 상태가 "경고"인 설비만 찾아 출력
for (
    name,
    info,
) in factory_equipment.items():  # .items()를 사용해 설비명과 상세 정보를 동시에 가져옴
    if info["status"] == "경고":
        print(f"상태 경고인 설비: {name}")
print("-" * 70)

print("\n=== 실습 7 - 표 데이터를 딕셔너리로 변환하기 ===")
# ①한 줄에 "센서명,측정값" 형태인 행 문자열들을 리스트로 저장
# ②for로 각 행을 쉼표로 split해 이름과 값으로 나누기
# ③이름을 키, 값을 숫자로 바꿔 딕셔너리에 추가
ls = ["온도", 78.5, "진동", 4.8, "압력", 2.1]

print("-" * 70)

print("\n=== 실습 8 - 센서 데이터 통합 정리 ===")
# ①센서 측정값 딕셔너리와 임계값 딕셔너리 저장
# ②values로 전체 평균 구하기
# ③items 순회로 임계값 초과 센서를 셋에 모으기
# ④셋을 정렬해 출력
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
    {"센서 이름": "conveyor_load", "하중": 450, "속도": 1.2},
]

limits = {
    "진동": 5.0,
    "온도": 80.0,
    "압력": 10.0,
    "유량": 50.0,
    "속도": 1500,
    "전류": 20.0,
    "소음": 85.0,
    "회전수": 3500,
    "점도": 45.0,
    "전압": 230.0,
    "하중": 400,
}
