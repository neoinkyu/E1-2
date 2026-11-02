
from quiz import Quiz


def get_default_quizzes():
    """기본 파이썬·Git 퀴즈 10개를 생성합니다."""

    return [
        Quiz(
            question="화면에 글자를 출력하는 파이썬 함수는?",
            choices=["input()", "print()", "open()", "type()"],
            answer=2,
            hint="입력과 출력은 서로 다른 함수가 담당합니다."
        ),
        Quiz(
            question="'hello'의 자료형은 무엇인가요?",
            choices=["int", "bool", "str", "list"],
            answer=3,
            hint="따옴표로 묶인 데이터의 자료형을 생각하세요."
        ),
        Quiz(
            question="파이썬에서 리스트를 나타내는 기호는?",
            choices=["[]", "{}", "()", "''"],
            answer=1,
            hint="여러 값을 순서대로 저장할 때 사용하는 자료형입니다."
        ),
        Quiz(
            question="조건에 따라 코드를 실행하는 키워드는?",
            choices=["for", "while", "def", "if"],
            answer=4,
            hint="조건의 참과 거짓에 따라 실행 경로가 달라집니다."
        ),
        Quiz(
            question="조건이 참인 동안 반복하는 구문은?",
            choices=["for", "if", "while", "class"],
            answer=3,
            hint="반복 횟수보다 조건 자체가 중요한 경우입니다."
        ),
        Quiz(
            question="파이썬에서 클래스를 정의하는 키워드는?",
            choices=["def", "class", "import", "return"],
            answer=2,
            hint="객체의 속성과 메서드를 묶는 설계도입니다."
        ),
        Quiz(
            question="새 Git 저장소를 초기화하는 명령어는?",
            choices=["git init", "git add", "git commit", "git push"],
            answer=1,
            hint="프로젝트에서 Git 관리를 처음 시작할 때 사용합니다."
        ),
        Quiz(
            question="변경사항을 로컬 Git 이력에 기록하는 명령은?",
            choices=["git add", "git push", "git pull", "git commit"],
            answer=4,
            hint="스테이징 영역에 파일을 추가한 다음 실행합니다."
        ),
        Quiz(
            question="원격 저장소의 변경사항을 가져와 반영하는 명령은?",
            choices=["git push", "git clone", "git pull", "git status"],
            answer=3,
            hint="원격 저장소에 업로드하는 작업과 반대 방향입니다."
        ),
        Quiz(
            question="새 브랜치를 만들면서 이동하는 명령은?",
            choices=[
                "git checkout main",
                "git checkout -b feature/quiz-play",
                "git merge feature/quiz-play",
                "git branch -d feature/quiz-play"
            ],
            answer=2,
            hint="브랜치 이동 명령에 생성 옵션을 함께 사용합니다."
        )
    ]


if __name__ == "__main__":
    quizzes = get_default_quizzes()

    assert len(quizzes) == 10
    assert all(
        len(q.choices) == 4 and 1 <= q.answer <= 4 and q.hint
        for q in quizzes
    )

    print(f"✅ 기본 퀴즈 {len(quizzes)}개 검증 완료!")
    print("\n첫 번째 문제 미리보기:")
    quizzes[0].display()
