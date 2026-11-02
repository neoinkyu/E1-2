
class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제를 입력해야 합니다.")

        if (
            not isinstance(choices, list)
            or len(choices) != 4
            or any(not isinstance(c, str) or not c.strip() for c in choices)
        ):
            raise ValueError("선택지는 빈칸 없이 4개여야 합니다.")

        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답은 1~4 사이의 정수여야 합니다.")

        if not isinstance(hint, str):
            raise ValueError("힌트는 문자열이어야 합니다.")

        self.question = question.strip()
        self.choices = [c.strip() for c in choices]
        self.answer = answer
        self.hint = hint.strip()

    def display(self):
        print(f"\n📝 {self.question}")

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, selected_answer):
        return selected_answer == self.answer

    def show_hint(self):
        if self.hint:
            print(f"💡 힌트: {self.hint}")
        else:
            print("등록된 힌트가 없습니다.")


if __name__ == "__main__":
    quiz = Quiz(
        question="Python에서 화면에 문자를 출력하는 함수는?",
        choices=["input()", "print()", "len()", "type()"],
        answer=2,
        hint="화면에 결과를 보여주는 함수입니다."
    )

    quiz.display()
    quiz.show_hint()

    assert quiz.is_correct(2) is True
    assert quiz.is_correct(1) is False

    print("\n✅ Quiz 클래스 테스트 통과!")
