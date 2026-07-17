# 🏭 POSCO K-뉴딜 PDM 아카데미

> **[K뉴딜] 설비 고장을 예측하는 AI 데이터 분석** 과정 학습 아카데미 📚
> 제조 설비 센서 데이터로 **이상 탐지 · 고장 예측 · 잔여수명(RUL)** 까지 🔧

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Field](https://img.shields.io/badge/Predictive%20Maintenance-예지보전-8A2BE2)
![Status](https://img.shields.io/badge/진행중-Python%20기초%20완료-brightgreen)
![Period](https://img.shields.io/badge/2026.07~2026.10-600hr-blue)

---

## 📖 소개

- 포스코 **K-뉴딜 예지보전(PDM, Predictive Maintenance) 아카데미** 수업 내용 정리하는 레포임
- 코딩 처음부터 시작 → Python 기초 → 시계열 분석 → **설비 이상 탐지 · 고장 예측** 까지 가는 게 목표 🎯
- 수업 실습 코드(Python, Ipynb) / AI 교과서식 정리 복습 노트 여기 모아둠 🗃️
- 예제가 죄다 `온도 · 진동 · 압력` 같은 설비 센서 데이터 기반임 (도메인 냄새 폴폴 남 😎)

## 🎯 과정 정보

| 항목 | 내용 |
| --- | --- |
| 🏷️ 과정명 | [K뉴딜] 설비 고장을 예측하는 AI 데이터 분석 |
| 🔢 차수 | 26-001 (취업예정자 > K뉴딜 > 초급) |
| 📅 교육기간 | 2026.07.06 ~ 2026.10.27 |
| ⏱️ 학습시간 | 600시간 (주간) |
| 📍 지역 | 포항 |
| ✅ 수료기준 | 출석율 80% 이상 |

## 🗺️ 학습 로드맵

- [x] 🐍 **Python 기초** — 출력 · 연산자 · 오류 읽기 · 변수 · 자료형 · 입력/형변환 · 문자열
- [ ] 📊 데이터 처리 & 기초 통계 · 시각화
- [ ] 📈 시계열 데이터 분석 (추세 · 주기 · 변동성)
- [ ] ⚙️ 제조 설비 · 센서 데이터 / 디지털 트윈 이해
- [ ] 🚨 이상 탐지(Anomaly Detection) 알고리즘
- [ ] 🔮 고장 예측 & 잔여수명(RUL) 예측 모델링
- [ ] 🛠️ 팀 프로젝트 — 스마트 정비 시스템 구현 & 최종 발표

## 🗂️ 폴더 구조

```text
posco-pdm-academy/
├── 🐍 Python/            # 수업 실습 코드 (.py) — 개념별 1파일
│   ├── 01_print.py           # print 내장 함수 · f-string
│   ├── 02_operator.py        # 산술 연산자
│   ├── 03_error.py           # 오류(Traceback) 읽는 법
│   ├── 04_variable.py        # 변수 선언 · 재할당
│   ├── 05_object.py          # 자료형 (int · float · str · bool)
│   ├── 06_operator2.py       # 연산자 심화 (비교 · 논리)
│   ├── 07_input.py           # 입력 · 형변환
│   ├── 08_string.py          # 문자열 (이스케이프 · 인덱싱 · 슬라이싱 · 연산)
│   └── etc.py                # 문자열 슬라이싱 심화 연습
├── ✍️ Practice/          # 개념별 연습문제 풀이 (수업 코드와 분리)
│   ├── 02_01~02_04_example.py # 변수 · 자료형 · 연산자 · 입력 실습
│   └── 03_01~03_03_example.py # 문자열 실습
├── 📓 Ipynb/             # Jupyter 노트북 (수업 · 연습)
│   ├── 2026.07.14 수업.ipynb
│   └── 월드컵_예측.ipynb        # 연습용 예측 노트북 ⚽
├── 🔁 Remind/            # 복습용 교과서식 정리 자료 (.pdf)
│   ├── 파이썬_데이터분석_문법교과서.pdf
│   ├── 파이썬기초_Git첫걸음.pdf
│   ├── Git과GitHub_실전.pdf
│   ├── 자료형과_연산자.pdf
│   └── 입력_형변환_문자열.pdf
├── 🧠 STT/               # 강의 음성 STT 기록 보관용 (예정)
├── 🤖 [LN_02~05]_Lab_*.ipynb # 딥러닝 강의 Lab 노트북 (Colab)
├── 📄 README.md              # 이 문서
├── 🐙 git cheatsheet.md      # Git 자주 쓰는 명령어 정리
└── 📌 COMMIT_CONVENTION.md   # 이 레포 커밋 메시지 규칙
```

> 🙈 `Lecture/`(강의 PDF 원본), `etc/`(스크린샷)는 `.gitignore` 처

### 📁 디렉토리 역할 한눈에

| 디렉토리 | 역할 | 담기는 파일 |
| --- | --- | --- |
| `Python/` | 수업에서 **개념을 처음 배우며 친 실습 코드**. 개념 1개 = 파일 1개 | `.py` |
| `Practice/` | 배운 개념을 **스스로 문제로 풀어본 연습**. 수업 코드와 섞지 않음 | `.py` |
| `Ipynb/` | 셀 단위 실행이 필요한 **주피터 수업·연습 노트북** | `.ipynb` |
| `Remind/` | 나중에 다시 보려고 만든 **교과서식 복습 정리본** | `.pdf` |
| `STT/` | 강의 음성을 텍스트로 옮긴 **STT 기록 보관용** (아직 비어 있음) | (예정) |
| 루트 `[LN_*]` | 딥러닝 과정 **Colab Lab 노트북** 원본 | `.ipynb` |

## 🐍 지금까지 배운 것

- **`print()`** — 내장 함수, f-string, `,` vs `+` 출력 차이 📤
- **산술 연산자** — `+  -  *  /  //  %  **`, 괄호로 연산 우선순위 지정 🧮
- **오류 읽기** — `Traceback`은 **맨 아래가 진짜 에러 위치**, `SyntaxError` / `NameError` 구분 🐞
- **변수** — 선언 · 재할당 · 값 복사 · 다중 할당, `=`는 "같다"가 아니라 **"저장"** 📦
- **자료형** — `int · float · str · bool` 특징과 `type()`으로 타입 확인 🔢
- **비교 · 논리 연산자** — `>  <  ==  !=`, `and · or · not` 로 조건 판별 ⚖️
- **입력 · 형변환** — `input()`은 무조건 `str` → `int()` / `float()`로 변환 🔀
- **문자열** — 이스케이프(`\n` `\t`) · 인덱싱 · 슬라이싱(`[start:end]`) · `len()` · 연산·검색 🔤
- **Github 기초** — git `init` · `status` · `add` · `commit` · `push` · `pull` 👊

> 💡 실습 예제 전부 설비 점검 리포트(`온도 / 진동 / 압력`) 컨셉으로 짬 → 뒤에 센서 데이터 분석으로 자연스럽게 이어짐.

## 🛠️ 기술 스택

**지금** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white)

**예정** &nbsp;![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C) ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

---

<div align="center">

✍️ **by [namelesspark](https://github.com/namelesspark)** · 🎓 


## 취업까지 열심히 화이팅!

</div>
