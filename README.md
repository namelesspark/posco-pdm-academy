# ⬡ POSCO K-뉴딜 PDM 아카데미

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Field](https://img.shields.io/badge/Predictive%20Maintenance-예지보전-8A2BE2)
![Status](https://img.shields.io/badge/진행중-Python%20기초-brightgreen)
![Period](https://img.shields.io/badge/2026.07~2026.10-600hr-blue)

---

## ❖ 소개

```
과정    [K뉴딜] 설비 고장을 예측하는 AI 데이터 분석 · 600시간
경로    코딩 입문 ⇢ Python 기초 ⇢ 시계열 분석 ⇢ 이상 탐지 ⇢ 고장 예측 · RUL
데이터  온도 · 진동 · 압력 등 제조 설비 센서 값
구성    수업 실습 코드(Python · Practice · Ipynb) + 교과서식 복습본(Remind)
용도    수업 기록 · 복습 · 포트폴리오
```

## ⬡ 과정 정보

| 항목 | 내용 |
| --- | --- |
| 과정명 | [K뉴딜] 설비 고장을 예측하는 AI 데이터 분석 |
| 차수 | 26-001 (취업예정자 › K뉴딜 › 초급) |
| 교육기간 | 2026.07.06 ⇢ 2026.10.27 |
| 학습시간 | 600시간 (주간) |
| 지역 | 포항 |
| 수료기준 | 출석율 80% 이상 |

## ⟡ 학습 로드맵

| 진행 | 단계 | 범위 |
| --- | --- | --- |
| `▰▰▰▰▰▰▱` | **Python 기초 문법** | 출력 · 연산자 · 오류 · 변수 · 자료형 · 입력 · 문자열 · 리스트 |
| `▱▱▱▱▱▱▱` | 데이터 처리 · 기초 통계 · 시각화 | Sandbox에서 AI4I 데이터셋 선행 실험 중 |
| `▱▱▱▱▱▱▱` | 시계열 데이터 분석 | 추세 · 주기 · 변동성 |
| `▱▱▱▱▱▱▱` | 설비 · 센서 데이터 이해 | 디지털 트윈 |
| `▱▱▱▱▱▱▱` | 이상 탐지 | Anomaly Detection |
| `▱▱▱▱▱▱▱` | 고장 예측 · 잔여수명 | RUL 모델링 |
| `▱▱▱▱▱▱▱` | 팀 프로젝트 | 스마트 정비 시스템 · 최종 발표 |

잔여 — 조건문(if) · 반복문(for) ⇢ Python 기초 마무리

## ◈ 폴더 구조

```text
posco-pdm-academy/
├── Python/                   수업 실습 코드 · 개념 1개 = 파일 1개
│   ├── 01_print.py             print · f-string · , vs +
│   ├── 02_operator.py          산술 연산자
│   ├── 03_error.py             오류(Traceback) 읽기
│   ├── 04_variable.py          변수 선언 · 재할당 · 값 복사
│   ├── 05_object.py            자료형 · type()
│   ├── 06_operator2.py         연산자 심화 · 비교 · 논리 · 복합 할당
│   ├── 07_input.py             입력 · 형변환
│   ├── 08_string.py            문자열 · 이스케이프 · 인덱싱 · 슬라이싱
│   └── 09_list.py              리스트 · 추가/제거 · 정렬 · copy()
├── Practice/                 개념별 연습문제 풀이 · 수업 코드와 분리
│   ├── 02_01 ~ 02_04_example.py  변수 · 자료형 · 연산자 · 입력
│   ├── 03_01 ~ 03_06_example.py  문자열 생성 ⇢ 슬라이싱 ⇢ 검색 ⇢ 정리 ⇢ f-string
│   └── 04_01_example.py          리스트
├── Ipynb/                    주피터 노트북
│   ├── 2026.07.14 수업.ipynb
│   └── 월드컵_예측.ipynb          연습용 예측 노트북
├── Remind/                   교과서식 복습 정리본 (.pdf)
│   ├── 파이썬_데이터분석_문법교과서.pdf
│   ├── 파이썬기초_Git첫걸음.pdf
│   ├── Git과GitHub_실전.pdf
│   ├── 자료형과_연산자.pdf
│   ├── 입력_형변환_문자열.pdf
│   ├── 문자열정리_메서드와_fstring.pdf
│   └── 리스트.pdf
├── Sandbox/                  수업 진도와 별개 실험 공간
│   ├── ai4i2020.csv              AI4I 2020 예지보전 데이터셋 (UCI)
│   ├── machine_learning.ipynb    데이터셋 직접 분석
│   ├── 파이썬_챌린지_문제.py       추가 연습 문제
│   ├── 파이썬_챌린지_정답.py
│   └── 연습.py
├── README.md
└── git cheatsheet.md         Git 자주 쓰는 명령어
```

로컬 전용 · 원격 제외 (`.gitignore`)

```
Lecture/                          강의 교안 원본 (저작권)
etc/                              스크린샷
STT/                              수업 음성 전사 원문
Python/etc.py                     슬라이싱 심화 낙서
COMMIT_CONVENTION.md              커밋 메시지 규칙 (개인 메모)
Sandbox/predictive-maintenance-ai4i/   참고용 외부 레포 (MIT)
```

### ⧉ 디렉토리 역할

| 디렉토리 | 역할 | 파일 |
| --- | --- | --- |
| `Python/` | 수업에서 개념을 처음 배우며 친 코드 | `.py` |
| `Practice/` | 배운 개념을 스스로 문제로 풀어본 연습 | `.py` |
| `Ipynb/` | 셀 단위 실행이 필요한 수업 · 연습 노트북 | `.ipynb` |
| `Remind/` | 나중에 다시 보려고 만든 교과서식 정리본 | `.pdf` |
| `Sandbox/` | 실제 설비 데이터셋을 직접 만져보는 실험실 | `.csv` · `.ipynb` |

## ⬢ 학습 현황

| 단원 | 배운 것 | 코드 |
| --- | --- | --- |
| 출력 | `print()` · f-string · `,` vs `+` 차이 | `01_print.py` |
| 연산자 | `+ - * / // % **` · 우선순위 · 복합 할당 `+=` | `02` · `06_operator2.py` |
| 오류 | Traceback은 **맨 아래가 진짜 원인** · `SyntaxError` `NameError` `ValueError` | `03_error.py` |
| 변수 | 선언 · 재할당 · 값 복사 · 다중 할당 · `=`는 "같다"가 아니라 **저장** | `04_variable.py` |
| 자료형 | `int` `float` `str` `bool` · `type()`으로 확인 | `05_object.py` |
| 비교 · 논리 | `> < == !=` · `and` `or` `not` ⇢ 결과는 항상 `bool` | `06_operator2.py` |
| 입력 · 형변환 | `input()`은 무조건 `str` ↦ `int()` `float()`로 변환 | `07_input.py` |
| 문자열 기초 | 이스케이프 · 인덱싱 · 슬라이싱 `[start:end:step]` · `len` `in` `count` `find` | `08_string.py` |
| 문자열 정리 | `upper` `lower` `strip` `replace` `split` `join` · 원본은 안 바뀜 | `03_04~06_example.py` |
| 리스트 | 인덱싱 · 슬라이싱 · `append` `insert` `extend` · `remove` `pop` `del` · `sort` · **참조 vs `copy()`** | `09_list.py` |
| Git | `init` `status` `add` `commit` `push` `pull` · `.gitignore` | `git cheatsheet.md` |

실습 예제는 전부 설비 점검 리포트(`온도 / 진동 / 압력`) 컨셉 ⇢ 뒤의 센서 데이터 분석으로 그대로 연결

## ⌑ 기술 스택

**현재** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white) ![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white)

**예정** &nbsp;![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C) ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

---

<div align="center">

**[namelesspark](https://github.com/namelesspark)** · 취업까지 완주

</div>
