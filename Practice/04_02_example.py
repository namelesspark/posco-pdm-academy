# print("=== 실습 - 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성하기 ===")

# age = input("나이를 입력하세요: ")

# if int(age) >= 19:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")


# print("\n=== 숫자 맞추기 게임 ===")
# import random

# num = -1
# answer = random.randint(1, 11)
# while answer != num:
#     num = int(input("💯숫자 맞추기 게임💯\n정수 입력하세요(1~10):"))
#     if num == answer:
#         print("정답입니다..")
#         break
#     else:
#         print("틀렸습니다.\n")


# print("\n=== 신호등 횡단 안내 ===")
# is_go = input("신호등 색: ")
# if is_go == "초록색":
#     print("건너")
# elif is_go == "빨간색":
#     print("멈춰")


# user_a = float(input("체온을 입력하세요: "))

# if user_a > 36.9:
#     print("고열")
# elif user_a >= 36.2 and user_a <= 36.9:
#     print("정상체온")
# else:
#     print("저체온")

# print("\n=== 실습 2 - 설비 온도 상태 판정하기 ===")
# temp = float(input("측정 온도 값 입력: "))

# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")


# print("\n=== 실습 3 - 두 조건을 모두 만족하는지 검증하기 ===")
# uid = str(input("초기 아이디 입력: "))
# upw = str(input("초기 비밀번호 입력: "))

# login_id = str(input("계정 아이디: "))
# login_pw = str(input("계정 비밀번호: "))

# if uid == login_id:
#     if upw == login_pw:
#         print(f"{login_id}/{login_pw} 로그인 성공")
#     else:
#         print("로그인 실패")
# else:
#     print("로그인 실패")


print("\n=== 실습 5 - 세 값으로 설비 종합 상태 판정하기 ===")
temp = float(input("온도: "))
vib = float(input("진동: "))
elec = float(input("전류: "))

if temp > 80 or vib > 4.0:
    print("위험: 즉시 정지")
elif elec > 60 and temp > 70:
    print("주의: 부하 점검")
elif vib > 2.5:
    print("주의: 진동 관찰")
else:
    print("정상")
