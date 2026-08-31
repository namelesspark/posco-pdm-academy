print("=== 실습 1 - 첫 함수 만들고 호출하기 ===")


def start_checking():
    print("점검을 시작합니다")


start_checking()
start_checking()
start_checking()


print("\n=== 실습 2 - 반복 코드를 함수로 정리하기 ===")


def start_checking():
    print("점검을 시작합니다")


def repeat_checking():
    start_checking()
    start_checking()
    start_checking()


repeat_checking()


def start_check():
    print("점검을 시작합니다")
    print("안전 장비를 확인하세요")
    print("기록을 준비하세요")


start_check()


print("\n=== 실습 3 - 함수 실행 흐름 추적하기 ===")


print("\n=== 실습 4 - 함수로 설비 점검 자동화하기 ===")


def print_line():
    print("=" * 80)


def print_check():
    print("점검 안내 출력")


# 장비 1
print_line()
print_check()
