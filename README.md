Quizzler App

An interactive Quiz Application built with Python, Tkinter, and Open Trivia Database API. This app fetches real-time questions from the API and provides an engaging UI with score tracking, feedback colors, and an optional timer.

✨ Features

✅ Dynamic Questions: Questions pulled from Open Trivia DB

✅ True/False Interface with visual feedback

✅ Score Tracking: Displays current score dynamically

✅ Progress Tracking: Indicates quiz progress

✅ Clean UI with color feedback for correct/wrong answers

✅ End Screen when the quiz is finished

✅ Responsive Delay: Automatic transition after feedback

🛠 Tech Stack

Python 3.8+

Tkinter for GUI

requests for API calls

📂 Project Structure
Quizzler/
├── main.py           # Entry point, initializes quiz logic and UI
├── question_model.py # Question class definition
├── quiz_brain.py     # Quiz logic (score, question flow)
├── ui.py             # Tkinter-based user interface
└── images/
    ├── true.png      # True button image
    └── false.png     # False button image
