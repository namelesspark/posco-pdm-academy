import pandas as pd

# 교안 16_02 - IQR 이상치 처리와 중복 데이터 실습
# Source files are included in lesson order.


###############################################################################
# Source: 16_02_01_iqr_59_260824_7.py
###############################################################################

import pandas as pd

df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')
print(df.head(3))

# 실린더압력 컬럼의 IQR 활용
q1 = df['실린더압력'].quantile(0.25)
q3 = df['실린더압력'].quantile(0.75)
print(f"Q1: {q1}, Q3: {q3}")
# Q1: 215.75, Q3: 265.0
iqr = q3 - q1
print(f"IQR: {iqr}")
# IQR: 49.25

# 상한선과 하한선은 IQR의 1.5배를 적용한다
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"하한선: {lower}, 상한선: {upper}")
# 하한선: 141.875, 상한선: 338.875


###############################################################################
# Source: 16_02_02_lower_upper_59_260824_8.py
###############################################################################

import pandas as pd

df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')
print(df.head(3))

# 사이클타임 컬럼의 IQR 활용
q1 = df['사이클타임'].quantile(0.25)
q3 = df['사이클타임'].quantile(0.75)
print(f"Q1: {q1}, Q3: {q3}")
# Q1: 215.75, Q3: 265.0
iqr = q3 - q1
print(f"IQR: {iqr}")
# IQR: 49.25

# 상한선과 하한선은 IQR의 1.5배를 적용한다
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"하한선: {lower}, 상한선: {upper}")
# 하한선: 141.875, 상한선: 338.875

# 상한선과 하한선을 이용해서 필터링할 조건을 만들 수 있다.
# 상한선~하한선 안쪽 : 정상범위로 판단
# 상한선과 하한선 바깥 : 이상하다고 판단 -> mask
mask = (df['사이클타임'] < lower) | (df['사이클타임'] > upper)
print(mask.sum()) # 6개는 정상범위 밖 확인
print(df[mask].shape) # (6, 7) : 6개 이상한 것들의 df
print(df[~mask].shape) # (196, 7) : ~은 NOT이라는 여집합을 의미 -> 정상범위 

# 정상범위는 다음의 마스크를 사용해도 됨
mask_ok = (df['사이클타임'] >= lower) & (df['사이클타임'] <= upper)
print(df[mask_ok].shape) # (182, 7) : 이 경우는 결측치는 제외함


###############################################################################
# Source: 16_02_03_mask_59_260824_9.py
###############################################################################

import pandas as pd

df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')
print(df.head(3))



# 사이클타임 컬럼의 IQR 활용
q1 = df['사이클타임'].quantile(0.25)
q3 = df['사이클타임'].quantile(0.75)
print(f"Q1: {q1}, Q3: {q3}")
# Q1: 215.75, Q3: 265.0
iqr = q3 - q1
print(f"IQR: {iqr}")
# IQR: 49.25

# 상한선과 하한선은 IQR의 1.5배를 적용한다
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"하한선: {lower}, 상한선: {upper}")
# 하한선: 141.875, 상한선: 338.875

# 상한선과 하한선을 이용해서 필터링할 조건을 만들 수 있다.
# 상한선~하한선 안쪽 : 정상범위로 판단
# 상한선과 하한선 바깥 : 이상하다고 판단 -> mask
mask = (df['사이클타임'] < lower) | (df['사이클타임'] > upper)

df_clean = df[~mask] # 이상한걸 제외한 나머지 멀쩡한 결과들 : 이상치 제거하기
print(len(df), len(df_clean)) # 202 196 -> 6개의 이상치 제거 확인
print(df_clean['사이클타임'].mean()) # 이상치가 제거된 값들의 평균 27.275824175824173

# 경계값으로 보정하기
# clip(lower, upper) 보정: 하한보다 작으면 하한값으로, 상한보다 크면 상한값으로 강제 평탄화(Windsorizing)합니다. 시계열 신호나 추세가 깨지지 않고 데이터 수도 그대로 유지되는 현업 다빈도 기법입니다.
df['사이클타임_clipped'] = df['사이클타임'].clip(lower = lower, upper = upper)
print(df['사이클타임_clipped'].agg(['min', 'max', 'mean']))
# min     20.600000
# max     58.612500
# mean    28.275931

# 결측치로 바꿔 채우기
# - mask(조건) + fillna(중앙값): 이상치를 일단 빈칸(NaN)으로 강제 변환한 뒤, 중앙값으로 부드럽게 채워 넣어 수치 왜곡을 차단합니다.
s_masked = df['사이클타임'].mask(mask)
s_masked.info()
print(s_masked.head())
print(s_masked.isna().sum()) # 20
s_fixed = s_masked.fillna(s_masked.median()) # 중앙값을 계산할때 NaN은 제외한다
print(s_fixed.mean()) # 26.802970297029702


###############################################################################
# Source: 16_02_04_duplicated_59_260824_10.py
###############################################################################

import pandas as pd

df = pd.read_csv('data/16_diecasting.csv', encoding='utf-8')
print(df.head(3))


# - df.duplicated(): 데이터프레임 내에서 완벽하게 내용이 겹쳐서 존재하는 중복 행 여부를 불리언 시리즈로 반환합니다.
print(df.duplicated()) # True/Flase의 Boolean Serise
print(df[df.duplicated()]) # "완전"중복된 row들만 df로 추려내기
#       샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0 -> 2건
# 201  89  235.0  1137.0   22.7   13.0  261.0   0 -> 2건

# 중복 개수 확인하기
print(df.duplicated().sum()) # 2 row들이 중복으로 더 존재함 (먼저 확인row 제외)
print(len(df)) # 202 : 전체가 202개 row로 2개 중복 빼면 순수하게 200개가 한줄씩 안겹치고 존재

print(df.duplicated(keep = False).sum()) # 4개의 중복 row들을 모두 제거 대상으로 삼기!

# 중복 제거
# - drop_duplicates(): 중복된 행들을 한 행만 남기고 깔끔하게 도려내는 함수입니다. subset=['샷'] 인자를 통해 특정 컬럼(예: 샷 번호 고유값)을 기준으로 유일성 검사를 할 수 있습니다.
# - reset_index(drop=True): 중복을 지운 후 듬성듬성 깨져버린 원래의 일련번호 인덱스를 0부터 시작하는 촘촘한 정수로 새로 깔끔하게 정렬해 줍니다.
print(len(df.drop_duplicates().reset_index(drop = True)))

# 부분중복 사례 제거 : '샷', '실린더압력', '주조압력' 컬럼만 중복되면 제거 대상!
print(len(df.drop_duplicates(subset = ['샷', '실린더압력', '주조압력'], keep = 'last').reset_index(drop = True)))


###############################################################################
# Source: 16_02_05_practice_59_260824_11.py
###############################################################################

import pandas as pd

CD = 'data/16_diecasting.csv'
WD = 'data/16_welding.csv'

df = pd.read_csv(CD)

# 실습 1. IQR과 이상치 경계 구하기
# 사이클타임의 IQR과 1.5배 규칙 하한·상한 계산
# IQR과 1.5배 규칙으로 이상치 경계를 구하기

# 단계
# · 사이클타임의 25%·75% 값을 구해 IQR(Q3-Q1) 계산
Q1 = df['사이클타임'].quantile(0.25)
Q3 = df['사이클타임'].quantile(0.75)

# · Q1에서 IQR의 1.5배를 빼 하한 계산
# · Q3에 IQR의 1.5배를 더해 상한 계산
IQR = Q3 - Q1
print(round(Q1, 2), round(Q3, 2), round(IQR, 2)) # 20.8 35.92 15.12
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(round(lower, 2), round(upper, 2)) # -1.89 58.61

# 예상 결과
# 사이클타임 IQR 15.12, 하한 -1.9·상한 58.6

print("----------------------------")

# 실습 2. 조건 필터로 이상치 골라내고 개수·비율
# 경계 밖 값을 조건으로 골라 개수와 비율 확인

# 단계
# · 하한보다 작거나 상한보다 큰 조건을 각각 괄호로 감싸 또는(|)로 연결
mask = (df['사이클타임'] < lower) | (df['사이클타임'] > upper)

# · 조건에 맞는 이상치 행만 골라 확인
print(df[mask][['샷', '사이클타임', '상태']])
#        샷   사이클타임  상태
# 146  147   125.9   0
# 180  181   652.3   1
# 181  182    93.1   1
# 190  191    91.2   1

# · sum으로 개수, mean으로 비율 계산
print(mask.sum(), round(mask.mean() * 100, 1)) # 6 3.0

# 예상 결과
# 사이클타임 이상치 6건, 비율 3.0%

print("----------------------------")

# 실습 3. 박스플롯으로 이상치 확인
# 박스플롯 수염 밖 점이 조건으로 고른 값과 같은지 확인
# 박스플롯으로 이상치를 그림으로 확인

# · 사이클타임 열을 박스플롯으로 그리기
# · 수염 밖에 찍힌 점의 위치 확인
# · 조건으로 고른 이상치와 그림의 점이 일치하는지 대조

# 예상 결과
# 수염 밖 점(6170 등 급증 샷)이 조건으로 고른 값과 일치

# --> 다음 단원에서 다룰 matplotlib 라이브러리 사용 예제라 건너뜀

print("----------------------------")

# 실습 4. 이상치 제거 후 크기 비교
# 경계 밖 행을 빼고 남은 크기와 평균 확인

# 단계
# · 조건을 뒤집어 정상 범위 행만 남기기
정상 = df[~mask]

# · 원본과 제거 후의 행 수를 비교
print(len(df), len(정상))  # 202 196

# · 제거 후 평균을 구해 변화 확인
print(round(df['사이클타임'].mean(), 2)) # 64.75
print(round(정상['사이클타임'].mean(), 2)) # 27.28

# 예상 결과
# 202행 → 196행, 제거 후 사이클타임 평균 27.28

print("----------------------------")

# 실습 5. 경계값 보정 clipping
# 이상치를 버리지 않고 경계값으로 눌러 보정

# 단계
# · clip으로 하한보다 작은 값은 하한으로 올리기
# · 상한보다 큰 값은 상한으로 내리기
보정 = df['사이클타임'].clip(lower=lower, upper=upper)

# · 보정 후 최솟값·최댓값·평균 확인
print(round(보정.min(), 2), round(보정.max(), 2))   # 20.6 58.61
print(round(보정.mean(), 2)) # 28.28

# 예상 결과
# 보정 후 최소 20.6·최대 58.6, 평균 28.28


###############################################################################
# Source: 16_02_06_practice_59_260824_12.py
###############################################################################

import pandas as pd

CD = 'data/16_diecasting.csv'
WD = 'data/16_welding.csv'

df = pd.read_csv(CD)

# 실습 1. IQR과 이상치 경계 구하기
# 사이클타임의 IQR과 1.5배 규칙 하한·상한 계산
# IQR과 1.5배 규칙으로 이상치 경계를 구하기

# 단계
# · 사이클타임의 25%·75% 값을 구해 IQR(Q3-Q1) 계산
Q1 = df['사이클타임'].quantile(0.25)
Q3 = df['사이클타임'].quantile(0.75)

# · Q1에서 IQR의 1.5배를 빼 하한 계산
# · Q3에 IQR의 1.5배를 더해 상한 계산
IQR = Q3 - Q1
print(round(Q1, 2), round(Q3, 2), round(IQR, 2)) # 20.8 35.92 15.12
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(round(lower, 2), round(upper, 2)) # -1.89 58.61

# 예상 결과
# 사이클타임 IQR 15.12, 하한 -1.9·상한 58.6

print("----------------------------")

# 실습 2. 조건 필터로 이상치 골라내고 개수·비율
# 경계 밖 값을 조건으로 골라 개수와 비율 확인

# 단계
# · 하한보다 작거나 상한보다 큰 조건을 각각 괄호로 감싸 또는(|)로 연결
mask = (df['사이클타임'] < lower) | (df['사이클타임'] > upper)

# · 조건에 맞는 이상치 행만 골라 확인
print(df[mask][['샷', '사이클타임', '상태']])
#        샷   사이클타임  상태
# 146  147   125.9   0
# 180  181   652.3   1
# 181  182    93.1   1
# 190  191    91.2   1

# · sum으로 개수, mean으로 비율 계산
print(mask.sum(), round(mask.mean() * 100, 1)) # 6 3.0

# 예상 결과
# 사이클타임 이상치 6건, 비율 3.0%

print("----------------------------")

# 실습 3. 박스플롯으로 이상치 확인
# 박스플롯 수염 밖 점이 조건으로 고른 값과 같은지 확인
# 박스플롯으로 이상치를 그림으로 확인

# · 사이클타임 열을 박스플롯으로 그리기
# · 수염 밖에 찍힌 점의 위치 확인
# · 조건으로 고른 이상치와 그림의 점이 일치하는지 대조

# 예상 결과
# 수염 밖 점(6170 등 급증 샷)이 조건으로 고른 값과 일치

# --> 다음 단원에서 다룰 matplotlib 라이브러리 사용 예제라 건너뜀

print("----------------------------")

# 실습 4. 이상치 제거 후 크기 비교
# 경계 밖 행을 빼고 남은 크기와 평균 확인

# 단계
# · 조건을 뒤집어 정상 범위 행만 남기기
정상 = df[~mask]

# · 원본과 제거 후의 행 수를 비교
print(len(df), len(정상))  # 202 196

# · 제거 후 평균을 구해 변화 확인
print(round(df['사이클타임'].mean(), 2)) # 64.75
print(round(정상['사이클타임'].mean(), 2)) # 27.28

# 예상 결과
# 202행 → 196행, 제거 후 사이클타임 평균 27.28

print("----------------------------")

# 실습 5. 경계값 보정 clipping
# 이상치를 버리지 않고 경계값으로 눌러 보정

# 단계
# · clip으로 하한보다 작은 값은 하한으로 올리기
# · 상한보다 큰 값은 상한으로 내리기
보정 = df['사이클타임'].clip(lower=lower, upper=upper)

# · 보정 후 최솟값·최댓값·평균 확인
print(round(보정.min(), 2), round(보정.max(), 2))   # 20.6 58.61
print(round(보정.mean(), 2)) # 28.28

# 예상 결과
# 보정 후 최소 20.6·최대 58.6, 평균 28.28

print("----------------------------")

# 실습 6. 처리 전후 통계 비교
# 제거·보정·중앙값 채움 세 처리의 평균 변화 비교
# - 실린더압력 열에 대해 원본 상태, 행 제거 상태, clip 보정 상태, 그리고 중앙값 채움 상태의 평균 변화를 정밀 대조합니다.

# 단계
# · 실린더압력 이상치 경계와 조건을 만들기
Q1 = df['실린더압력'].quantile(0.25)
Q3 = df['실린더압력'].quantile(0.75)
IQR = Q3 - Q1
L = Q1 - 1.5 * IQR
U = Q3 + 1.5 * IQR

m = (df['실린더압력'] < L) | (df['실린더압력'] > U)
채움 = df['실린더압력'].mask(m).fillna(df['실린더압력'].mask(m).median())


# · 제거·보정·중앙값 채움 세 방식을 각각 적용
# · 처리 전 평균과 세 방식의 평균을 나란히 비교
print(round(df['실린더압력'].mean(), 2)) # 234.31 (처리전)
print(round(df[~m]['실린더압력'].mean(), 2)) # 238.39 (mask로 제거)
print(round(df['실린더압력'].clip(L, U).mean(), 2)) # 235.31
print(round(채움.mean(), 2)) # 238.05

# 예상 결과
# 전 234.31 → 제거 238.39·보정 235.31·채움 238.05


print("----------------------------")

# 실습 7. duplicated로 중복 찾기와 개수
# 완전 중복 행을 찾고 keep 옵션에 따른 개수 비교

# · duplicated로 중복 행 여부를 참·거짓으로 표시 -> Boolean Series
# · sum으로 중복 개수 세고 중복 행 직접 확인
print(df.duplicated().sum()) # 2
print(df[df.duplicated()])
#       샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 200   8  215.0  1038.0   20.9   11.0  258.0   0
# 201  89  235.0  1137.0   22.7   13.0  261.0   0

# · keep을 거짓으로 두면 겹친 행이 모두 표시되는 것 확인
print(df.duplicated(keep=False).sum()) # 4 : 겹친 행을 원본까지 모두 표시 

# 예상 결과
# 완전 중복 2건, keep을 끄면 겹친 행 4건 표시


print("----------------------------")

# 실습 8. drop_duplicates로 중복 제거
# 완전 중복 제거와 기준 컬럼 지정 제거를 비교

# · drop_duplicates로 완전 중복 행 제거
# · 제거 후 행 수와 남은 중복 개수 확인
print(len(df)) # 202
df_onlyone = df.drop_duplicates()
print(len(df_onlyone)) # 200

# · subset으로 특정 컬럼만 기준 삼아 제거
df_onlyone_shot = df.drop_duplicates(subset=['샷'], keep='last')
print(len(df_onlyone_shot)) # 200

# 예상 결과
# 202행 → 200행, 남은 중복 0, subset 기준도 200행

print("----------------------------")

# 실습 9. reset_index로 인덱스 정리
# 중복 제거로 생긴 인덱스 구멍을 다시 매기기
# 중복 제거로 생긴 인덱스 구멍을 0부터 다시 매기기

# · drop_duplicates로 중복을 제거
df_clean = df.drop_duplicates()

# · reset_index로 인덱스를 0부터 다시 매기기
df_clean_idxreset = df_clean.reset_index(drop = True)

print(df_clean.index.min(), df_clean.index.max()) # 0 199
print(len(df_clean)) # 200

print(df_clean_idxreset.index.min(), df_clean_idxreset.index.max()) # 0 199
print(len(df_clean_idxreset)) # 200

# · 인덱스 최솟값·최댓값으로 연속성 확인

# 예상 결과
# 인덱스 0~199로 연속, 최종 200행


print("----------------------------")
# 실습 10. 다른 현장(용접) 이상치·중복 종합 정제
# 탐색→보정→중복 점검→저장을 다른 현장에 그대로
# IQR 탐색부터 정제 데이터 저장까지 한 흐름으로

# - 실무 용접 설비의 '통전전류' 컬럼에 IQR 규칙을 적용하여 이상 전류 경계선을 구하고, 약 14.8%의 불량 전류 샷을 정상 범위로 보정(clip)하는 정제 파이프라인입니다.
# - 그와 함께 중복 측정된 로그들을 제거하고 인덱스를 새롭게 정리하여 깨끗해진 최종 데이터를 'cleaned_welding.csv' 파일로 저장함으로써 전처리 과정을 일괄 완성합니다.
# - 도메인 컨텍스트: 용접 전류가 너무 낮으면 판재가 붙지 않고, 너무 높으면 구멍이 뚫려 불량이 나므로 IQR 이탈 전류를 잡아 clipping 전처리하는 것이 머신러닝 학습 전 성능 안정화의 핵심입니다.

# 용접전압,용접전류,통전전압,통전전류,가압력,판정
# 308,7962,364,5975,9270,1
# 308,7934,359,6020,9324,1
# 320,8287,359,6113,9275,1

# · 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인
wf = pd.read_csv(WD)
c = '통전전류'

q1, q3 = wf[c].quantile(0.25), wf[c].quantile(0.75)
lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
m = (wf[c] < lo) | (wf[c] > hi)
print(int(m.sum()), round(m.mean() * 100, 1)) # 24 14.8 (판정 0 불량과 대체로 일치)

# · clip으로 이상치를 보정하고 중복을 제거·정리
wf[c] = wf[c].clip(lower=lo, upper=hi)
wf = wf.drop_duplicates().reset_index(drop=True)
print(len(wf)) # 158

# · 정제한 데이터를 파일로 저장
wf.to_csv('data/16_welding_cleaned.csv', index=False)

# 예상 결과
# 용접 통전전류 이상치 24건(14.8%), 보정·중복 제거 후 저장
