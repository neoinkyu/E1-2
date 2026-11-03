
# 🎯 파이썬·Git 기초 퀴즈 게임

> Codyssey E1-2 | 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기

## 1. 프로젝트 개요

Python 기본 문법과 객체지향 프로그래밍을 학습하기 위해 개발한 콘솔 기반 퀴즈 게임입니다.

사용자는 퀴즈를 풀거나 새로운 문제를 추가·삭제할 수 있으며, 최고 점수와 게임 기록을 확인할 수 있습니다.

JSON 파일을 활용하여 프로그램 종료 후에도 데이터가 유지되도록 구현했습니다. 개발 과정은 Git과 GitHub로 관리했습니다.

### 개발 환경

- Python 3.10 이상
- Visual Studio Code
- Git / GitHub
- 외부 라이브러리 없음 (Python 표준 라이브러리 사용)

## 2. 퀴즈 주제 및 선정 이유

**주제: 파이썬·Git 기초 지식**

프로그래밍 입문 과정에서 학습한 내용을 직접 퀴즈 문제로 제작하고 반복 학습하기 위해 선정했습니다.

Python의 변수, 자료형, 조건문, 반복문, 클래스와 Git의 주요 명령어 등을 다룹니다.

기본 퀴즈는 총 10문제이며, 사용자 등록 기능으로 문제를 추가할 수 있습니다.

## 3. 주요 기능

| 메뉴 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 랜덤 출제, 문제 수 선택, 정답 판정 |
| 2 | 퀴즈 추가 | 문제, 선택지, 정답, 힌트 등록 |
| 3 | 퀴즈 목록 | 등록된 문제와 선택지 조회 |
| 4 | 퀴즈 삭제 | 번호 선택, 삭제 확인, 파일 반영 |
| 5 | 최고 점수 확인 | 최고 점수 및 상세 기록 조회 |
| 6 | 게임 기록 조회 | 날짜별 게임 결과를 최신순 표시 |
| 7 | 종료 | 데이터 저장 후 정상 종료 |

### 추가 구현 기능

- 랜덤 출제: `random.sample()`으로 중복 없이 문제 선택
- 문제 수 선택: 전체 문제 중 원하는 개수 선택
- 힌트 제공: 정답 입력 시 `h` 입력
- 힌트 감점: 힌트 사용 후 정답이면 기본 배점의 50% 획득
- 점수 히스토리: 게임 날짜, 문제 수, 정답 수, 점수 저장
- 오류 처리: 잘못된 입력, Ctrl+C, EOF 및 JSON 파일 손상 대응

### 점수 계산

100점 만점을 기준으로 계산합니다.

- 힌트 없이 정답: 문제당 1점
- 힌트 사용 후 정답: 문제당 0.5점
- 오답: 0점

최종 점수 = (획득한 배점 합계 / 출제 문제 수) × 100

## 4. 설치 및 실행 방법

### GitHub 저장소 복제

```bash
git clone https://github.com/neoinkyu/E1-2.git
cd E1-2
```

### 프로그램 실행

```bash
python main.py
```

Python 3.10 이상이 설치되어 있어야 합니다.

별도의 패키지 설치 과정은 필요하지 않습니다.

### 이용 방법

1. 메인 메뉴에서 1~7번 선택
2. 퀴즈 풀기에서 원하는 문제 수 입력
3. 정답 번호(1~4) 입력 또는 `h`로 힌트 확인
4. 게임 완료 후 결과 및 최고 점수 확인
5. 7번 선택 시 데이터 저장 후 종료

## 5. 프로젝트 파일 구조

```text
E1-2/
├── main.py
├── quiz.py
├── quiz_game.py
├── quiz_play.py
├── default_quizzes.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
```

| 파일 | 역할 |
|---|---|
| `main.py` | 메인 메뉴 및 프로그램 실행 |
| `quiz.py` | 개별 퀴즈를 관리하는 Quiz 클래스 |
| `quiz_game.py` | 게임 전체 관리, 등록·삭제·저장·조회 |
| `quiz_play.py` | 출제, 입력 처리, 힌트, 점수 계산 |
| `default_quizzes.py` | 기본 퀴즈 10개 |
| `state.json` | 퀴즈, 최고 점수, 게임 기록 저장 |
| `.gitignore` | Git 관리 제외 파일 설정 |
| `docs/screenshots/` | 실행 및 Git 실습 증빙 이미지 |

`state.json`은 프로그램 실행 과정에서 생성되며, GitHub에는 업로드하지 않습니다.

## 6. 데이터 저장 방식

프로젝트 루트의 `state.json`에 UTF-8 인코딩으로 데이터를 저장합니다.

### 데이터 구조 예시

```json
{
  "quizzes": [
    {
      "question": "화면에 글자를 출력하는 파이썬 함수는?",
      "choices": ["input()", "print()", "open()", "type()"],
      "answer": 2,
      "hint": "입력과 출력은 서로 다른 함수가 담당합니다."
    }
  ],
  "best_score": 75,
  "history": [
    {
      "played_at": "2026-11-03T09:00:00+09:00",
      "score": 75,
      "correct_count": 2,
      "total_questions": 2,
      "hint_used_count": 1
    }
  ]
}
```

위 데이터는 구조 설명용 예시입니다.

- `quizzes`: 문제, 선택지, 정답, 힌트 목록
- `best_score`: 최고 점수 (100점 만점)
- `history`: 게임 완료 시각과 성적 기록

파일이 없으면 기본 퀴즈를 사용합니다. 읽을 수 없는 파일은 가능한 경우 백업한 뒤 기본 데이터로 시작합니다.

`state.json`은 `.gitignore`에 포함되어 있으므로 PC마다 게임 기록이 별도로 관리됩니다.

## 7. 프로그램 실행 화면

### 메인 메뉴

![메인 메뉴](docs/screenshots/02-main-menu.png)

### 퀴즈 풀기

![퀴즈 풀기](docs/screenshots/03-quiz-play.png)

### 힌트 기능

![힌트](docs/screenshots/04-hint.png)

### 게임 결과

![게임 결과](docs/screenshots/05-quiz-result.png)

### 퀴즈 추가

![퀴즈 추가](docs/screenshots/07-add-quiz.png)

### 퀴즈 목록

![퀴즈 목록](docs/screenshots/08-quiz-list.png)

### 퀴즈 삭제

![퀴즈 삭제](docs/screenshots/09-delete-quiz.png)

### 최고 점수

![최고 점수](docs/screenshots/10-best-score.png)

### 게임 기록

![게임 기록](docs/screenshots/11-game-history.png)

### 데이터 영속성

![데이터 저장 및 복원](docs/screenshots/12-data-persistence.png)

### 입력 오류 처리

![입력 오류 처리](docs/screenshots/13-error-handling.png)

## 8. Git 및 GitHub 활용

기능 단위로 코드를 작성하고 테스트한 뒤 커밋했습니다.

개발 과정에서 다음 Git 명령어를 학습하고 활용했습니다.

`init`, `add`, `commit`, `push`, `pull`, `checkout`, `merge`

퀴즈 출제 기능은 `feature/quiz-play` 브랜치에서 개발한 뒤 `main` 브랜치에 병합했습니다.

### 브랜치 병합 기록

![브랜치 병합](docs/screenshots/06-git-merge.png)

## 9. 학습 내용 및 개발 경험

이번 프로젝트를 통해 다음 내용을 학습했습니다.

- 변수, 자료형, 조건문, 반복문, 함수
- 클래스, 객체, 속성, 메서드
- 리스트와 딕셔너리를 활용한 데이터 관리
- JSON 파일 입출력 및 데이터 영속성
- try/except를 활용한 예외 처리
- Git의 버전 관리 및 브랜치 병합
- GitHub를 통한 여러 PC 간 개발 코드 동기화

특히 프로그램의 기능을 역할별로 나누고, 구현한 기능을 단계별로 검증하면서 개발하는 과정을 경험했습니다.

## 10. 개발 저장소

[GitHub - neoinkyu/E1-2](https://github.com/neoinkyu/E1-2)

## 11. Git clone 및 pull 실습

별도 디렉터리에 저장소를 복제하여 README를 수정하고 커밋했습니다.
