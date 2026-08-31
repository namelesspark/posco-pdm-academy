# print("\n=== 실습 1 - range로 숫자 흐릅 출력하기 ===")
# n = int(input("정수 입력: "))

# l = []
# for i in range(n):
#     l.append(i + 1)
# print(l)

# l = []
# for i in range(2, n, 2):
#     l.append(i)
# print(l)

# l = []
# for i in range(n, 0, len-1):
#     l.append(i)
# print(l)


# print("\n=== 369 게임 출력 ===")
# bounds = str(input("입력: "))
# bounds_len = len(bounds)  # 몇자리수인지 확인하기 위함

# l = []  # 빈 리스트
# count_369 = 0
# for num in range(1, int(bounds) + 1):

#     str_num = str(num)
#     len_num = len(str_num)

#     for j in range(0, len(str_num)):
#         if (  # 각 인덱스 자리수 3, 6, 9 포함 확인
#             str_num[j] == "3" or str_num[j] == "6" or str_num[j] == "9"
#         ):
#             count_369 += 1

#     if count_369 > 0:
#         l.append("짝" * count_369)
#     else:
#         l.append(num)

#     count_369 = 0


# print(f"369 결과: {l}")


# print("\n=== 실습 2 - 반복으로 1부터 N까지 합계 구하기 ===")
# n = int(input("정수 입력: "))

# total = 0
# for i in range(1, n + 1):
#     total += i
# print(total)


# print("\n=== 실습 3 - 중첩 반복으로 구구단 출력하기 ===")
# for i in range(2, 10):
#     print(f"\n{i}단")
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i*j}")

# print("\n=== 실습 4 - 기준을 초과하는 값 개수 세기 ===")
# count = int(input("측정 획수 입력: "))

# over = 0
# l = []
# for i in range(count):
#     num = float(input(f"측정값 입력({i+1}번): "))
#     l.append(num)
#     if num > 80:
#         over += 1
# print(f"측정 횟수: {count} / 측정값: {l} / 초과 개수: {over}")


print("\n=== 실습 3 번외 - 중첩 반복으로 구구단 출력하기 ===")
print("=== 조건: 2의 배수단만 출력 ===")
for i in range(2, 10, 2):
    print(f"\n{i}단")
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")
