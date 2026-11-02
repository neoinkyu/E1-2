
import json
from datetime import datetime
from pathlib import Path

from default_quizzes import get_default_quizzes
from quiz import Quiz
from quiz_play import play_quiz, get_number


def get_required_text(prompt):
    """빈칸이 아닌 문자열을 입력받습니다."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("⚠️ 빈 내용은 입력할 수 없습니다.")


class QuizGame:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent / "state.json"
        self.quizzes = get_default_quizzes()
        self.best_score = None
        self.history = []
        self.can_save = True

        self.load_state()

    def load_state(self):
        """저장된 퀴즈, 최고 점수, 게임 기록을 불러옵니다."""
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 구조가 올바르지 않습니다.")

            items = data["quizzes"]
            best_score = data["best_score"]
            history = data["history"]

            if not isinstance(items, list) or not isinstance(history, list):
                raise ValueError("퀴즈 또는 기록 목록이 올바르지 않습니다.")

            if best_score is not None and (
                type(best_score) is not int or not 0 <= best_score <= 100
            ):
                raise ValueError("최고 점수가 올바르지 않습니다.")

            if any(not isinstance(item, dict) for item in history):
                raise ValueError("게임 기록 형식이 올바르지 않습니다.")

            loaded_quizzes = [
                Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"],
                    item.get("hint", "")
                )
                for item in items
            ]

            self.quizzes = loaded_quizzes
            self.best_score = best_score
            self.history = history

            print(f"📂 저장된 퀴즈 {len(self.quizzes)}개를 불러왔습니다.")

        except FileNotFoundError:
            print("📂 첫 실행입니다. 기본 퀴즈 10개를 사용합니다.")

        except (OSError, ValueError, TypeError, KeyError) as error:
            print(f"⚠️ 저장 파일을 읽을 수 없습니다: {error}")

            backup_name = (
                "state.corrupt-"
                + datetime.now().strftime("%Y%m%d-%H%M%S-%f")
                + ".json"
            )
            backup_path = self.file_path.with_name(backup_name)

            try:
                self.file_path.replace(backup_path)
                print(f"📦 기존 파일을 {backup_name}으로 백업했습니다.")
                print("기본 퀴즈 데이터로 시작합니다.")
            except OSError:
                self.can_save = False
                print("⚠️ 백업에 실패하여 기존 파일 보호를 위해 저장을 중단합니다.")

    def save_state(self):
        """데이터를 JSON 파일에 저장합니다."""
        if not self.can_save:
            print("⚠️ 기존 데이터 보호를 위해 저장이 차단되었습니다.")
            return False

        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                    "hint": quiz.hint
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "history": self.history
        }

        temp_path = self.file_path.with_name("state.json.tmp")

        try:
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            temp_path.replace(self.file_path)
            return True

        except OSError as error:
            print(f"⚠️ 데이터 저장 실패: {error}")
            return False

    def play(self):
        """퀴즈를 진행하고 점수를 기록합니다."""
        result = play_quiz(self.quizzes)

        if result is None:
            return

        score = result["score"]

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

        record = {
            "played_at": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            **result
        }

        self.history.append(record)

        if self.save_state():
            print("💾 게임 결과가 저장되었습니다.")

    def add_quiz(self):
        """새로운 퀴즈를 등록하고 저장합니다."""

        print("\n========================================")
        print("📌 새로운 퀴즈 등록")
        print("========================================")

        question = get_required_text("문제를 입력하세요: ")

        choices = []
        for number in range(1, 5):
            choice = get_required_text(f"선택지 {number}: ")
            choices.append(choice)

        answer = get_number("정답 번호 (1~4): ", 1, 4)

        hint = get_required_text("힌트를 입력하세요: ")

        try:
            new_quiz = Quiz(
                question=question,
                choices=choices,
                answer=answer,
                hint=hint
            )
        except ValueError as error:
            print(f"⚠️ 퀴즈 등록 실패: {error}")
            return

        self.quizzes.append(new_quiz)

        if self.save_state():
            print("\n✅ 새로운 퀴즈가 등록되었습니다!")
            print(f"📋 전체 퀴즈: {len(self.quizzes)}개")
            print("💾 데이터 저장 완료")
        else:
            self.quizzes.pop()
            print("⚠️ 저장 실패로 퀴즈 등록을 취소했습니다.")


