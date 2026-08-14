def check(name, value, danger=90, warn=80, unit="도"):
    """측정값을 기준과 비교해 (판정, 근거) 튜플을 돌려준다.

    danger / warn / unit 은 기본값 인자라 생략 가능하다.
    """
    if value >= danger:
        verdict = "위험"
        reason = f"{value} >= 위험기준 {danger}"
    elif value >= warn:
        verdict = "주의"
        reason = f"{value} >= 주의기준 {warn}"
    else:
        verdict = "정상"
        reason = f"{value} < 주의기준 {warn}"

    return verdict, reason


records = [
    ("압축기_A", 88, {}),
    ("펌프_B",   95, {}),
    ("송풍기_C", 88, {"danger": 85}),
    ("절단기_D", 79, {"warn": 75, "unit": "bar"}),
]

print("=" * 58)
print("           유연한 설비 판정 함수")
print("=" * 58)

for name, value, opt in records:
    verdict, reason = check(
        name,
        value,
        danger=opt.get("danger", 90),
        warn=opt.get("warn", 80),
        unit=opt.get("unit", "도"),
    )
    unit = opt.get("unit", "도")
    print(f"{name}: {value}{unit} -> {verdict} ({reason})")

print("-" * 58)
# 압축기_A 와 송풍기_C 는 측정값이 똑같이 88 이지만 판정이 다르다.
#   압축기_A: danger 기본값 90 을 그대로 씀 -> 88 < 90 이라 "주의"
#   송풍기_C: danger 를 85 로 덮어씀      -> 88 >= 85 라서 "위험"
# 즉 같은 값이라도 기준이 바뀌면 결과가 바뀐다.
print("같은 88인데 판정이 다른 이유: danger 기본값 90 vs 덮어쓴 85")

# verdict / reason 은 check 함수 안에서 만들어진 지역변수다.
# 함수 밖에서 그대로 쓸 수 있는 이유는 return 으로 내보내 받았기 때문.
# 만약 함수 안의 다른 지역변수를 밖에서 print 하면 NameError 가 난다.
print("지역변수는 return 으로 내보내야만 밖에서 쓸 수 있음")
print("=" * 58)
