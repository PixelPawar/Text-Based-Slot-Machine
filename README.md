# 🎰 Slot Machine Game (Python CLI)

A simple command-line based **Slot Machine Game** built using Python. This project simulates a casino-style slot machine where users can deposit money, place bets on multiple lines, and spin to try their luck.

---

## 🚀 Features

* 💰 Deposit system with input validation
* 🎯 Betting on 1 to 3 lines
* 🎲 Randomized slot machine spins
* 🧮 Winnings calculation based on symbol matches
* 📊 Balance tracking after each spin
* ⚠️ Input validation for all user entries

---

## 🛠️ Technologies Used

* Python (Core concepts)
* `random` module for slot generation

---

## 📂 Project Structure

```
slot_machine.py   # Main game file
```

---

## ▶️ How to Run

1. Make sure Python is installed
2. Save the file as `slot_machine.py`
3. Open terminal in the file directory
4. Run:

```bash
python slot_machine.py
```

---

## 🎮 How to Play

1. Enter the deposit amount
2. Choose number of lines (1–3)
3. Enter bet per line (₹200–₹10000)
4. Spin the slot machine
5. Win if all symbols in a line match

---

## 🎯 Game Logic

* The slot machine has **3 rows × 3 columns**
* Symbols:

  * A → appears 2 times, highest value
  * B → appears 4 times
  * C → appears 6 times
  * D → appears 8 times (lowest value)
* Matching all symbols in a row = win
* Winnings = `symbol_value × bet`

---

## 💡 Example Output

```
A | B | C
A | A | A
D | C | B

You won ₹1000
You won on lines: 2
```

---

## 🚀 Future Improvements

Here are some ideas to make your project more advanced:

### 🔹 1. Add GUI

* Use frameworks like:

  * Tkinter (basic)
  * PyQt (advanced)
  * Or even React + backend API (since you're into web dev)

---

### 🔹 2. Save User Data

* Store balance using:

  * File system (JSON)
  * SQLite / MySQL database
* Allow login system

---

### 🔹 3. Improve Game Mechanics

* Add:

  * Diagonal wins
  * Bonus rounds 🎁
  * Multipliers (e.g., x2, x5)
  * Jackpot system 💎

---

### 🔹 4. Better Randomness & Fairness

* Use weighted probability more realistically
* Add RTP (Return to Player) logic like real casinos

---

### 🔹 5. Add Sounds & Animations

* Simulate spinning effect using delays
* Add sound effects for wins

---

### 🔹 6. Unit Testing

* Use `unittest` or `pytest`
* Test:

  * Winning logic
  * Betting validation

---

### 🔹 7. Web Version (Highly Recommended 🚀)

Since you're learning web dev:

* Convert this into:

  * Backend: Node.js / Flask
  * Frontend: React
* Make it playable in browser

---

## 📌 Learning Outcomes

* Input validation in Python
* Working with lists and dictionaries
* Randomized simulations
* Game logic implementation
* Modular programming

---

## 🧑‍💻 Author

* PixelPawar

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

