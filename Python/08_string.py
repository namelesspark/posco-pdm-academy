# # ==================================================
# # 이스케이프 문자

# notice = "설비 점검 안내 \n1.전원 확인\n2. 센서 점검"
# print(notice)

# tap = "이름\t상태"
# print(tap)
# print("이름 상태")

# # ==================================================
# # 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# # 문자열[인덱스 번호]
# # 문자열의 첫 글자 인덱스는 0

# print("\n\n=== 인덱싱 ===")
# word = "PYTHON"
# print(word[0], word[1], word[2])

# abc = "abcdefghijklmnopqrstuvwxyz"
# # a0 b1 c2 d3 e4 / f5 g6 h7 i8 j9 / k10 l11 m12 n13-13 o14-12 / p15-11 q16-10 r17-9 s-8 t-7 / u-6 v-5 w-4 x-3 y-2 / z-1

# # 자기 이름 출력하기 ( parkminho )
# print(
#     abc[15] + abc[0] + abc[17] + abc[10] + abc[12] + abc[8] + abc[13] + abc[7] + abc[14]
# )

# print(
#     abc[-11]
#     + abc[0]
#     + abc[-9]
#     + abc[10]
#     + abc[12]
#     + abc[8]
#     + abc[13]
#     + abc[7]
#     + abc[-12]
# )

# # ================================================
# # 슬라이싱이란 - 여러 글자를 구간으로 잘라내기
# # 문자열[시작:끝]
# #
# print(word[1:4])


# # 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
# print(abc[len(abc) - 1])


# # 특정 문자열의 위치를 반환

# email = "jade.lake8852@gmail.com"
# at = email.index("@")

# print(email[0:at])


# # ================================================
# print("=== index() ===")


# # ================================================
# print("=== count() ===")

# # 문자열에서 특정 문자열의 개수 세기
# str = "a, b, c, d, e,a, a"

# str_cnt = str.count("a")
# print(str_cnt)

# # ,의 개수 세기
# print(str.count(","))
# print(str.count(", "))


# # SQE-00Q8이라는 설비의 SQE만 뽑아내기
# sqe = "SQE-00Q8"
# sqe_index = sqe.find("SQE")
# print(sqe_index)

# print(sqe[sqe_index : sqe_index + 3])


# print("=== Startswith, Endswith ===")

# # EQP로 시작하는지 확인해보기

# eqp = "EQP-00Q8"
# print("EQP-001".startswith("EQP"))
# print("EQP-001".endswith("001"))

# str2 = "월요일입니다. 여러분은 할 수 있어요!"
# print(str2.endswith)
# print(str2.endswith("!"))
# print(str2.endswith("요!"))
# print(str2.endswith(" 월요일입니다. 여러분은 할 수 있어요!"))


# print("=== 실험 ===")
# ex_1 = "Apple Application Apologize Apply Append"
# print(ex_1.find("Appli"))


# # ===============================
# print("=== 값은 객체다 ===")
# print(type("잊으면 안됨!"))


# # ===============================
# # endswith와 len의 차이는? - endswith는 변수 뒤 .을 붙여 사용하는 특정 기능의 함수, len은 내장 함수이다 .


print("=== UPPER ===")
word = "python"
print(word.upper())  # PYTHON
print(word.count("p"))  # 1
print(word.startswith("p"))  # True


# ===================================
# 재할당 복습
num = 1
num = num + 1

str = "apple"

print(str.upper())
str.upper()
print(str)

str = str.upper()
print(str)


# ===================================
print("=== capitalize() ===")
str = "park min ho"
print(str.capitalize())
print(str.title())

str = "i'\m person"
print(str.title())


# ===================================
# strip(), lstrip(), rstrip()
# 위치에 따라 공백을 다르게 지울 수 있다.

# strip으로 문자 제거
print("=== strip() ===")
str4 = "===정상==="
print(str4.strip("="))

str5 = "=정상============"
print(str5.strip("= "))
# strip 자체가 공백을 지우는 것이기 때문에
# 공백에 상관 없이 양 끝의 해당 문자열 삭제

str6 = "==정==상=="
print(str6.strip("="))
# 문자 사이 부터는 관여하지 않음


print("\n=== 실험 ===")
str8 = "aaab 이렇게? cd"
print(str8.strip("abcd"))
print(str8.strip("abcd "))
print(str8.strip("bc"))
print(str8.strip("ab"))


# =============================
print("=== replace() === ")
# 특정 문자를 치환할 때 사용
# .replace("바꾸고싶은 문자열", "바꿀 문자열")

print("정 상 가 동")
print("정 상 가 동".replace(" ", ""))

# 글자 치환
print("고장".replace("고장", "fault"))
print("고장".replace("고", "fault"))
