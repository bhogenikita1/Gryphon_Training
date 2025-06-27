from quiz_questions import generate_question
from quiz_exceptions import safe_integer_input
import time

def math_quiz_game():
    print("Welcome to the Math Quiz Game!")

    # Track name entry time
    start_name_time = time.time()
    name = input("Enter your name: ")
    end_name_time = time.time()
    name_time_taken = end_name_time - start_name_time

    print(f"\nHello, {name}! You took {name_time_taken:.2f} seconds to enter your name.")
    print("Let's begin the quiz!\n")

    score = 0

    while True:
        question, correct_answer = generate_question()
        print(question)

        # Track time before and after answering
        start_answer_time = time.time()
        user_answer = safe_integer_input("Your answer: ")
        end_answer_time = time.time()
        time_taken = end_answer_time - start_answer_time

        # Scoring logic
        if user_answer == correct_answer:
            score += 10
            print("✅ Correct! +10 points.")
        else:
            score -= 5
            print(f"❌ Wrong! The correct answer was {correct_answer}. -5 points.")

        print(f"🕒 You took {time_taken:.2f} seconds to answer.")
        print(f"🎯 Your current score: {score}\n")

        cont = input("Do you want to continue the quiz? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("\n👎 LOOSER")
            break

# Run the game
if __name__ == "__main__":
    math_quiz_game()
