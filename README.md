# Rock-Paper-Scissors Game (Python)

This repository contains a simple and interactive Python implementation of the classic **Rock-Paper-Scissors** game. The program allows the user to input their choice, compares it with the computer's randomly generated choice, and displays the result.

---

## 📌 Features

* Command-line based interactive game.
* Randomized computer moves using Python's `random` module.
* Clean and understandable logic structure.
* Immediate display of choices and game results.
* Beginner-friendly implementation.

---

## 🧠 Game Logic

This version uses the following numeric mapping for choices:

| Choice  | Value |
| ------- | ----- |
| Rock    | 1     |
| Paper   | -1    |
| Scizzor | 0     |

The program compares your choice with the computer's and prints whether you **win**, **lose**, or **tie**, based on predefined conditions.

---

## 📂 Code Structure

```
rock_paper_scizzor.py
├── Imports random module
├── Defines function: rock_paper_scizzor()
│   ├── Random computer choice
│   ├── User input
│   ├── Mapping of choices
│   ├── Print choices
│   ├── Conditional result logic
└── Calls the function
```

---

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Download or clone the repository:

   ```bash
   git clone <repository-link>
   ```
3. Navigate to the project folder:

   ```bash
   cd rock-paper-scizzor
   ```
4. Run the program:

   ```bash
   python3 rock_paper_scizzor.py
   ```

---

## 🕹️ Example Gameplay

```
Enter your choice: rock
Your choice: 1
Computer's choice: 0
You win !!!
```

---

## 📌 Future Improvements (Optional Ideas)

* Add input validation (e.g., prevent crashes for wrong inputs)
* Allow replay without restarting the program
* Add score tracking for multiple rounds
* Build a GUI version using Tkinter or PyGame
* Convert game logic to a class-based structure

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to submit an issue or create a pull request.

---

## 📜 License

This project is open-source and can be used freely for learning and experimentation.

---

Enjoy playing the game and improving your Python skills!
