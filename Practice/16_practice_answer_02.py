# =====================================================================
# 종합 실습 2. 실시간 측정값 입력 시스템
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

LIMIT = 100  # 임계값

quit_str = "q"
lst = []
warn_count = 0
total_val = 0
while True:
    val = input("측정값: ")

    if val == "q":
        break
    elif int(val) > 100:
        warn_count += 1
        print(f"경고💀 - LIMIT 초과 회수: {warn_count}")
    else:
        lst.append(int(val))
        total_val += int(val)

if len(lst) == 0:
    print("입력된 측정값이 없습니다.")
else:
    print(f"총 입력 개수: {len(lst)}")

    max_val = 0
    min_val = 0
    for i in range(len(lst)):
        if max_val < lst[i]:
            max_val = lst[i]

        if min_val > lst[i]:
            min_val = lst[i]

    print(f"최댓값: {max_val} / 최솟값: {min_val}")
    print(f"평균값: {total_val / len(lst):.1f}")
    print(f"임계값 초과 개수: {warn_count}")

    over_medium = 0
    om_list = []
    for i in range(len(lst)):
        if lst[i] > (total_val / len(lst)):
            over_medium += 1
            om_list.append(lst[i])

    print(f"평균보다 큰 값의 개수: {over_medium}")
    print(f"평균보다 큰 값 리스트: {om_list}")
    print(f"상위 3개 값: {lst[:3].sort(reverse=True)}")
