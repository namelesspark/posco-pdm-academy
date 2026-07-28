# list는 파이썬의 자료형 중 하나이다
# 문자열, 스트링, 플롯, 불리언처럼 list에도 method가 존재한다.

temps = [37, 38, 20, 55, 33]

# 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 빈 리스트도 가능
empty = []

# 리스트 안에 마지막 요소를 뽑고 싶다면?
print(mixed[-1])


# 리스트에 담긴 값의 개수 새기
# len() 내장 함수 사용
print(len(temps))  # 5
print(len(empty))  # 0

# 리스트에 담긴 값의 개수 변수에 적용
temps_len = len(temps)
print(temps_len)  # 5

# 리스트의 인덱스
print(temps[0], temps[-1])
# 처음 마지막 요소 출력

# -1을 사용하는 이유: 최신 값을 대체로 뒤에 추가된다.
# 가장 최신 값이 곧 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 -1로 계산이 가능하지만
# 이 작업이 번거로워 -1을 가장 많이 사용한다.

# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5]) - IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의해야 함

print(type(temps))  # <class 'list'>
print(type(temps[0]))  # <class 'int'>

float_temps = [36.5, 36.7, 36.9, 37.1, 37.2]
print(type(float_temps))  # <class 'list'>
print(type(float_temps[0]))  # <class 'float'>
# 리스트가 아닌 요소가 되는 순간, 그 하나의 값의 타입이 출력된다.

mixed = ["펌프", 7, True]
print(type)


# 리스트 슬라이싱
# 리스트명[시작:끝:간격] -> 세 개 다 생략 가능 == 문자열

temps = [35, 36, 37, 38]
print(temps[1:2])  # 요소 36만 나오지만, 리스트로 나온다 -> [36]
print(temps[1:2], temps[3:])  # [36] [38]


# ===================================
# in 연산자
# in 연산자로 값의 존재를 참 / 거짓으로 확인
# temps = [35, 36, 37, 38]
temps[2] = 999
print("2번 인덱스 값 변경 결과: " + str(temps[2]))

machines = ["펌프", "압축기", "모터"]
print("펌프" in machines)  # True
print("펌프" not in machines)  # False
