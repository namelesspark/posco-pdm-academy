# 🐙 Git / GitHub 자주 쓰는 명령어 치트시트

> 실무·수업에서 진짜 매일 쓰는 것만 추림. 위에서 아래로 흐름 순서대로 배치함.
> `<...>`는 직접 채워 넣는 값임 (예: `<branch>` → `main`).

---

## ⚙️ 0. 최초 세팅 (컴퓨터당 한 번만)

| 명령어 | 설명 |
| --- | --- |
| `git config --global user.name "이름"` | 커밋에 남길 이름 |
| `git config --global user.email "메일"` | 커밋에 남길 이메일 (GitHub 계정과 동일하게) |
| `git config --global init.defaultBranch main` | 기본 브랜치 이름을 `main`으로 |
| `git config --global core.editor "code --wait"` | 기본 편집기 VS Code로 (선택) |
| `git config --list` | 현재 설정 전체 확인 |

🪟 **Windows 사용자 추가 권장**

```bash
git config --global core.autocrlf true    # 줄바꿈(CRLF/LF) 자동 변환
```

---

## 🔐 인증 (push 하려면 필요)

HTTPS로 push할 때 비밀번호 대신 **토큰(PAT)** 또는 **GitHub CLI**를 씀.

```bash
# 방법 A) GitHub CLI 로그인 (제일 편함)
gh auth login

# 방법 B) Personal Access Token
# GitHub > Settings > Developer settings > Personal access tokens 에서 발급
# push 시 Username=깃허브아이디, Password=발급받은 토큰 입력
```

---

## 🚀 1. 저장소 시작

| 명령어 | 설명 |
| --- | --- |
| `git init` | 현재 폴더를 새 로컬 저장소로 만듦 |
| `git clone <url>` | 원격 저장소를 통째로 복제 |
| `git remote add origin <url>` | 로컬 저장소에 원격 주소 연결 |
| `git remote -v` | 연결된 원격 주소 확인 |

---

## 🔄 2. 기본 워크플로우 ⭐ (제일 많이 씀)

```bash
git status                 # 현재 상태 확인 (수시로 침)
git add <file>             # 특정 파일 스테이징
git add .                  # 변경분 전부 스테이징
git commit -m "메시지"      # 스테이징된 것 커밋
git commit -am "메시지"     # add + commit 한 번에 (추적 중인 파일만)
git push                   # 원격에 올리기
git pull                   # 원격 변경분 받아오기
```

🔁 **흐름 요약**

```text
작업파일 --add--> Staging --commit--> Local Repo --push--> Remote Repo
                                                <--pull--
```

---

## 🌿 3. 브랜치

| 명령어 | 설명 |
| --- | --- |
| `git branch` | 브랜치 목록 |
| `git switch <branch>` | 브랜치 이동 (구버전: `git checkout`) |
| `git switch -c <branch>` | 새 브랜치 만들고 바로 이동 |
| `git merge <branch>` | 현재 브랜치에 다른 브랜치 병합 |
| `git branch -d <branch>` | 브랜치 삭제 |
| `git push -u origin <branch>` | 새 브랜치 최초 push (업스트림 연결) |

---

## ↩️ 4. 되돌리기 / 수정

| 명령어 | 설명 |
| --- | --- |
| `git restore <file>` | 작업 중 변경 취소 (마지막 커밋 상태로) |
| `git restore --staged <file>` | `add` 취소 (스테이징만 해제) |
| `git commit --amend` | 방금 한 커밋 메시지·내용 수정 |
| `git reset --soft HEAD~1` | 마지막 커밋 취소, 변경분은 스테이징에 유지 |
| `git reset --mixed HEAD~1` | 마지막 커밋 취소, 변경분은 작업공간에 유지 (기본값) |
| `git reset --hard HEAD~1` | ⚠️ 마지막 커밋 + 변경분까지 완전 삭제 (복구 어려움) |
| `git revert <commit>` | 특정 커밋을 되돌리는 **새 커밋** 생성 (안전) |
| `git rm -r --cached <folder>` | 추적만 해제 (로컬 파일은 유지, `.gitignore`랑 세트) |

---

## 🔍 5. 확인 / 비교

| 명령어 | 설명 |
| --- | --- |
| `git log --oneline --graph --all` | 커밋 히스토리 한 줄 그래프로 |
| `git diff` | 아직 add 안 한 변경분 비교 |
| `git diff --staged` | 스테이징된 변경분 비교 |
| `git show <commit>` | 특정 커밋 상세 내용 |

---

## 📦 6. 임시 저장 (stash)

작업하다 급하게 브랜치 바꿔야 할 때, 커밋 없이 잠깐 치워두기.

```bash
git stash            # 현재 변경분 임시 저장 + 작업공간 깨끗이
git stash list       # 저장 목록
git stash pop        # 가장 최근 저장분 복원 + 목록에서 제거
```

---

## 🙈 7. .gitignore

버전관리에서 제외할 파일/폴더 지정. 저장소 루트에 `.gitignore` 파일로 둠.

```gitignore
# 폴더 통째로 제외
Lecture/

# 특정 확장자
*.log
*.env

# OS/편집기 부산물
.DS_Store
.vscode/
__pycache__/
```

> ⚠️ 이미 커밋된 파일은 `.gitignore`에 넣어도 안 빠짐 → `git rm -r --cached <경로>` 로 추적 먼저 해제해야 함.

---

## 🗓️ 전형적인 하루 흐름

```bash
git pull                       # 1. 최신 상태로 맞추기
git switch -c feature/login     # 2. 작업 브랜치 생성
# ... 코드 작업 ...
git status                     # 3. 뭐 바뀌었나 확인
git add .                      # 4. 스테이징
git commit -m "feat: 로그인 추가"  # 5. 커밋
git push -u origin feature/login  # 6. 원격에 올리기
# 7. GitHub에서 Pull Request 생성 → 리뷰 → merge
```

---

<div align="center">

📌 헷갈리면 `git status` 부터. 이게 지금 상태랑 다음에 뭐 할지 다 알려줌.

</div>
