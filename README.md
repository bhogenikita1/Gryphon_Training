# 🧠 BrainPlay Game 🎮

Welcome to **BrainPlay** – a fun, interactive math quiz game built in Python where your brain gets tested on **squares** and **square roots**, and your **speed** matters!

---

## 🚀 Features

✅ Reads and greets player by name  
✅ Tracks how long it takes to enter your name  
✅ Asks **random math questions**:  
  - What is the **square** of a number?  
  - What is the **square root** of a perfect square?  
✅ Questions range from 1 to 10000  
✅ Score:
- +10 for correct answers  
- -5 for wrong answers  
✅ Measures time taken to **answer each question**  
✅ Shows score and time after every round  
✅ Option to continue or quit anytime  
✅ If you quit: you'll be called a **LOOSER** (just for fun!)

---

## 🧩 Folder Structure

brainplay_game/

  │
  ├── main.py # Main game logic
  
  ├── quiz_questions.py # Module to generate quiz questions
  
  ├── quiz_exceptions.py # Module for safe input handling
  



---

## 🛠 Requirements

- Python 3.x installed  
- No external libraries required – just `random` and `time` modules from Python standard library.

---

## 💡 How to Run the Game

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Navigate to the folder containing `main.py`.
4. Run the game using:



## Sample Output

python main.py

Enter your name: Nikita

Hi Nikita, you took 2.15 seconds to enter your name.

What is the square root of 2025?

Your answer: 45

✅ Correct! +10 points.

🕒 You took 3.42 seconds to answer.

🎯 Current Score: 10

Do you want to continue the quiz? (yes/no): no

👎 LOOSER






