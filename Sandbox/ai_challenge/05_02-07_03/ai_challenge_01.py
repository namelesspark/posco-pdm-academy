# =====================================================================
# AI 챌린지 1. 생산 목표 도달 시뮬레이션
# while · break · continue · 무한루프 함정
# 자세한 요구사항은 README.md 참고
# =====================================================================

production = [120, 0, 95, 130, -5, 110, 88, 0, 140, 102, 97, 115]
TARGET = 800

i = 0
skipped = 0
count = 0
total = 0
# TODO 1. `while` 로 리스트를 앞에서부터 훑기 (`for` 쓰지 말 것 — 이 문제는 `while` 연습)
while i < len(production):
    i += 1
    # TODO 2. 값이 `0` 이하면 `continue` 로 건너뛰되, **건너뛴 횟수**를 따로 셀 것
    if production[i - 1] <= 0:
        skipped += 1
        continue
    # TODO 3. 정상 값이면 누적하고 `N회차: +값 (누적 X)` 형태로 출력
    elif production[i - 1] > 0:

        count += 1
        total += production[i - 1]
        print(f"{i}회차: +{production[i-1]} (누적 {total})")

    # TODO 4. 누적이 `TARGET` 이상이 되는 순간 `break`
    if total >= TARGET:
        break


# TODO 5. 반복이 끝난 뒤: 달성했으면 `목표 달성`, 못 했으면 `목표 미달` 출력
if total >= TARGET:
    print("목표 달성")
elif total < TARGET:
    print("목표 미달")
# TODO 6. 마지막에 유효 횟수 / 건너뛴 횟수 출력
print(f"유효 욋수: {count} / 건너뛴 횟수: {skipped}")

# 도전) `TARGET` 을 `2000` 으로 바꿔서 **끝까지 가도 미달**인 경우가 제대로 출력되는지 확인해보기.
