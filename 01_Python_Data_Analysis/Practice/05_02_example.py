# 종료 조건 3단계
# 시작 상태: 조건 변수의 출발 값 정하기
# 종료 조건: 멈춤 상태의 반대를 조건식으로
# 갱신 방법: 종료를 향해 값 바꾸기

# print("\n=== 실습 1 - while로 목표값 도달까지 반복하기 ===")
# import random

# answer = random.randint(1, 11)

# a = -1
# while answer != a:
#     a = int(input("맞출 때까지 입력:"))

#     if answer == a:
#         print("정답입니다!")

# print("\n=== 실습 - up down 게임 ===")
# # 1~50 중 하나의 숫자를 정답으로 저장
# # 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# # 정답일 시 "정답입니다", "게임 종료" 출력
# import random

# num = random.randint(1, 50)

# answer = 0
# found = False
# while found != True:
#     answer = int(input("정수 입력: "))
#     if answer > num:
#         print("down!")
#     elif answer < num:
#         print("up!")
#     else:
#         found = True
# print("정답입니다! 게임 종료")


# print("\n=== 실습 - 조건 반복 결합 흐름 읽기 ===")
# is_true = False
# total = 0
# i = 0
# while i < 3:
#     val = int(input("값 입력: "))

#     if val > 5:
#         is_true = True
#         print("참")
#     else:
#         is_true = False
#         print("거짓")

#     total += val
#     i += 1

# print(f"합계: {total}")


print("\n=== 실습 2 -  플래그로 조건 만족 값 검색하기 ===")
found = False
l = []
while found != True:
    count = int(input("측정 횟수 입력: "))

    for i in range(count):
        l.append(float(input("측정값 입력: ")))

        if l[i] > 80:
            found = True
            print("발견. 중단")
            break
        else:
            continue

    break
print(f"측정값: {l}")
