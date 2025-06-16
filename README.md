# ❄️ Snowman Meltdown

A fun terminal-based word-guessing game where your mission is to save a snowman from melting! Each incorrect letter guess causes part of the snowman (drawn with ASCII art) to melt. Guess the entire word before it's too late!

---

## 🧩 Features

- 🎲 Random word selection from a predefined word list
- 🖼 ASCII art that visually shows snowman melting over time
- ✅ Input validation (only accepts single alphabetical characters)
- 🔁 Replay option after each game
- 🧠 Full game logic with win/loss conditions
- 📦 Modular code structure for easy maintenance and extension

---

## 📁 Project Structure

```
Snowman-Meltdown/
├── snowman.py         # Main game logic and game loop
├── config/
│   └── config.py      # Contains the STAGES (ASCII art) and WORDS list
├── ascii_art.py       # (Optional) Alternative location for STAGES if separated
└── README.md          # You're reading it!
```

---

## ▶️ How to Play

1. Run the game:
   ```bash
   python snowman.py
   ```

2. You’ll be shown a masked word and ASCII art of a full snowman.

3. Type one letter at a time to guess the word.

4. For each incorrect guess, the snowman loses a piece.

5. The game ends when:
   - ✅ You guessed the whole word → You win!
   - ❌ The snowman fully melts → Game over!

6. After each round, you'll be asked if you'd like to play again.

---

## 📄 Game Modules

### `snowman.py`

- Starts the game
- Handles the game loop, input, mistake tracking, and win/loss conditions
- Calls helper functions for display and word selection

### `config/config.py`

- Contains:
  - `STAGES`: List of ASCII snowman stages for each mistake count
  - `WORDS`: List of possible secret words

---

## 🛠 Requirements

- Python 3.7 or later
- No external libraries needed

---

## 👨‍💻 Author

**Martin Haferanke**  
Created: 16.06.2025

---

## 📬 License

This game is free to use for educational or personal purposes.