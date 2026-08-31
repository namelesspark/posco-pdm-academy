print("\n=== 실습 2 - 다중 매개변수로 센서값 계산하기 ===")


def report_sensor_val(sensor1, sensor2):
    name1 = sensor1.get("이름")
    temp1 = sensor1.get("온도")

    name2 = sensor2.get("이름")
    temp2 = sensor2.get("온도")

    return (name1, temp1), (name2, temp2)


sensor1 = {"이름": "온도센서A", "온도": 24.5}
sensor2 = {"이름": "온도센서B", "온도": 30.2}

result1, result2 = report_sensor_val(sensor1, sensor2)
print(result1)
print(result2)


print("\n=== 실습 4 - 반환값으로 간단 계산기 만들기 ===")


def calc_oper(a, b):
    return a + b


num = calc_oper(10, 20)
print(num)
num2 = calc_oper(20, num)
print(num2)


print("\n=== 실습 5 - 센서 통계 함수 만들기 ===")


def calc_statistics(ls):
    mean = sum(ls) / len(ls)
    # or import statistics
    # statistics.mean(ls)
    return min(ls), max(ls), mean


ls = []
while True:
    v = input("센서 값 입력(q입력 시 입력 종료): ")
    if v == "q":
        break
    elif float(v):
        ls.append(float(v))
    else:
        ("입력값 오류")
        continue


print(calc_statistics(ls))
