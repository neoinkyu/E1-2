
import random


def get_number(prompt, minimum, maximum):
    """허용 범위 내의 숫자를 입력받습니다."""
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("⚠️ 숫자를 입력해주세요.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("⚠️ 올바른 숫자를 입력해주세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"⚠️ {minimum}~{maximum} 사이의 숫자를 입력해주세요.")


def get_answer(quiz):
    """정답 입력과 힌트 사용 여부를 처리합니다."""
    hint_used = False

    while True:
        user_input = input("정답 (1~4, h=힌트): ").strip().lower()

        if user_input == "h":
            if hint_used:
                print("⚠️ 이미 힌트를 사용했습니다.")
            elif quiz.hint:
                quiz.show_hint()
                hint_used = True
                print("ℹ️ 정답 시 배점의 50%를 획득합니다.")
            else:
                quiz.show_hint()
            continue

        if not user_input:
            print("⚠️ 정답 번호를 입력해주세요.")
            continue

        try:
            answer = int(user_input)
        except ValueError:
            print("⚠️ 1~4 사이의 숫자를 입력해주세요.")
            continue

        if 1 <= answer <= 4:
            return answer, hint_used

        print("⚠️ 1~4 사이의 숫자를 입력해주세요.")


def play_quiz(quizzes):
    """퀴즈를 출제하고 결과를 계산합니다."""

    if not quizzes:
        print("⚠️ 등록된 퀴즈가 없습니다.")
        return None

    print("\n🎯 퀴즈 풀기를 시작합니다!")
    print(f"현재 등록된 문제: {len(quizzes)}개")

    count = get_number(
        f"몇 문제를 풀까요? (1~{len(quizzes)}): ",
        1,
        len(quizzes)
    )

    selected_quizzes = random.sample(quizzes, count)

    correct_count = 0
    hint_count = 0
    earned_points = 0

    for index, quiz in enumerate(selected_quizzes, start=1):
        print("\n----------------------------------------")
        print(f"[문제 {index}/{count}]")

        quiz.display()
        answer, hint_used = get_answer(quiz)

        if hint_used:
            hint_count += 1

        if quiz.is_correct(answer):
            correct_count += 1

            if hint_used:
                earned_points += 0.5
                print("✅ 정답! (힌트 사용: 50% 배점)")
            else:
                earned_points += 1
                print("✅ 정답입니다!")
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

    score = round((earned_points / count) * 100)

    print("\n========================================")
    print("🏆 퀴즈 결과")
    print("========================================")
    print(f"출제 문제: {count}개")
    print(f"정답 개수: {correct_count}개")
    print(f"힌트 사용: {hint_count}회")
    print(f"최종 점수: {score}점 / 100점")
    print("========================================")

    return {
        "score": score,
        "correct_count": correct_count,
        "total_questions": count,
        "hint_used_count": hint_count
    }
