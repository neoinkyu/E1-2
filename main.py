
from default_quizzes import get_default_quizzes
from quiz_play import play_quiz


def show_menu():
    print("\n========================================")
    print("     🎯 파이썬·Git 기초 퀴즈 게임")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 퀴즈 삭제")
    print("5. 최고 점수 확인")
    print("6. 게임 기록 조회")
    print("7. 종료")
    print("========================================")


def get_menu_choice():
    while True:
        user_input = input("선택 (1~7): ").strip()

        if not user_input:
            print("⚠️ 번호를 입력해주세요.")
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print("⚠️ 숫자를 입력해주세요.")
            continue

        if 1 <= choice <= 7:
            return choice

        print("⚠️ 1~7 사이의 숫자를 입력해주세요.")


def main():
    quizzes = get_default_quizzes()

    while True:
        try:
            show_menu()
            choice = get_menu_choice()

            if choice == 1:
                play_quiz(quizzes)
            elif choice == 2:
                print("📌 퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print("📋 퀴즈 목록 기능은 준비 중입니다.")
            elif choice == 4:
                print("🗑️ 퀴즈 삭제 기능은 준비 중입니다.")
            elif choice == 5:
                print("🏆 최고 점수 기능은 준비 중입니다.")
            elif choice == 6:
                print("📊 게임 기록 기능은 준비 중입니다.")
            else:
                print("👋 퀴즈 게임을 종료합니다.")
                break

        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력이 중단되었습니다.")
            print("프로그램을 안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()
