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


print("\n=== 369 게임 출력 ===")
bounds = str(input("입력: "))
bounds_len = len(bounds)  # 몇자리수인지 확인하기 위함

l = []  # 빈 리스트
count_369 = 0
for num in range(1, int(bounds) + 1):

    str_num = str(num)
    len_num = len(str_num)

    for j in range(0, len(str_num)):
        if (  # 각 인덱스 자리수 3, 6, 9 포함 확인
            str_num[j] == "3" or str_num[j] == "6" or str_num[j] == "9"
        ):
            count_369 += 1

    if count_369 > 0:
        l.append("짝" * count_369)
    else:
        l.append(num)

    count_369 = 0


print(f"369 결과: {l}")


