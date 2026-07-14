# =============================================

# 오류는 읽을 정보다
# Traceback (most recent call last):
#   File "main.py", line 8, in <module>
#     order_coffee()
#   File "main.py", line 5, in order_coffee
#     make_coffee()
#   File "main.py", line 2, in make_coffee
#     print(10 / 0)
# ZeroDivisionError: division by zero

# 파이썬의 Traceback은 특이하게 가장 아래쪽이 진짜 에러가 발생한 위치이다.
# 위에서 아래로 갈수록 시간 순서대로 실행된 것을 의미한다.

# print(온도)
# NameError: name '온도' is not defined


# SyntaxError: 문법 오류
# NameError: 정의되지 않은 이름을 호출했을 때

# ========================================================
# SyntaxError 예시
# print("Hello World" '(' was never closed
# print("진동) unterminated string literal (detected at line ~~)

# 오류 대처 4단계
# 당황하지 않기
# 오류 메시지 읽기
# 오류 메시지 이해하기
# 오류 메시지 검색하기

# ========================================================

# 실습 - 오류 하나씩 고치기

# print(온도, 75)
# print("진동", 2.3
# print("압력": 4.0)

print("온도", 75)  # 따옴표 추가
print("진동", 2.3)  # 괄호 닫기
print("압력", 4.0)  # 콜론을 쉼표로 변경

# ========================================================

# 실습 - 점검 리포트 안내
Temperature_1st = 82  # 정상 온도
Temperature_Anomaly = 95  # 이상 온도
Temperature_Change = abs(Temperature_1st - Temperature_Anomaly)  # 온도 상승량

print("=====", "1번", "설비", "점검", "=====")
print("온도(℃):" + str(Temperature_1st))
print("온도 상승량((❁´◡`❁)):" + str(Temperature_Change))

# Temperature_1st, Temperature_Change은 숫자형이므로,
# + 연산자를 사용하려면 따옴표를 붙이거나,
# str() 클래스 호출 후 형변환이 필요함.
