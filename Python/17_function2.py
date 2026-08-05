import math


def say_hi(name):
    print(f"반갑습니다. {name}")


say_hi("Ned")
say_hi("Tuna")
say_hi("Layla")


# 예제 코드: 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
    print(f"{name} 장비의 점검을 시작합니다")


check("압축기A")
check("펌프B")


# 매개변수가 2개 이상인 예제 - 덧셈
def calc_sum(a, b):
    return a + b


print(calc_sum(5, 8))


# 매개변수가 2개 이상인 예제 - 장비, 온도 정보 출력
def report_keywords(name, temp):
    print(f"보고\n장비 이름: {name}\n장비 온도: {temp}")


report_keywords("펌프A", 37.4)
# C언어, Java는 아규먼트로 함수 파라미터에 어떻게 보냈는지 모른다
# 파이썬은 잘 명시할 수 있도록 만들었다
report_keywords(temp=37.4, name="펌프A")
# 순서가 바뀌었을 때 생겨나는 오류를 근본적으로 차단시켰다.


def calc_average(a, b):
    print(f"평균 온도: {(a + b ) / 2}")


avg = calc_average(75.3, 88.0)
print(avg)


import random


def get_random_group():
    group = [
        {"이름": "에스파", "리더": "카리나"},
        {"이름": "리센느", "리더": "원이"},
        {"이름": "엔믹스", "리더": "오해원"},
    ]

    my_group = random.choice(group)

    return my_group.get("이름"), my_group.get("리더")


group_name, group_leader = get_random_group()
print((f"{group_name}의 리더는 {group_leader}입니다"))

# 가봤거나, 가보고싶은 여행지 정보를 모아봅시다 최소 5개 이상
# 가봤거나, 가보고싶은 여행지 정보를 모아봅시다
# 함수를 호출하면 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다! 000 나라의 수도 000 입니다" 출력
