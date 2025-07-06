# 🎲 Twenty One - Dice Game

A command-line Python game inspired by *Blackjack* and traditional *dice games*, where players roll to reach a score as close to **21** as possible without going bust. This version includes custom gameplay rules and logic-based decision-making — perfect for practicing Python fundamentals with a fun twist.

---

## 🧩 Game Overview

**Twenty One** is a multiplayer turn-based dice game of chance and strategy. Players must decide whether to keep rolling or stop, balancing the risk of going bust with the desire to beat their opponents by getting closer to 21.

---

## 📝 Game Rules (Custom Variant)

- 🎯 **Goal**: Get as close to **21** as possible without exceeding it.
- 🎲 Each player starts with a **score of 0**.
- 🔁 The game is played in **rounds**, where each player gets **one turn per round**.
- 🎲 **Rolling Rules**:
  - Players **must roll two dice** if their current score is less than **14**.
  - Once a player has **14 or more**, they may choose to roll **one** or **two** dice.
- ⛔ If a player’s score goes **over 21**, they go **bust** and are eliminated.
- 🛑 Players can choose to **stop rolling** at any time and lock in their score.
- 🏆 The winner is the player whose final score is **closest to 21** without going bust.
- ❌ If **all players go bust**, or **multiple players tie** with the best score, **no one wins**.

---

## 🎮 Game Features

- Supports **multiple players** (local multiplayer via command line)
- Interactive prompts for roll decisions
- Dice-rolling simulation with random number generation
- Status display for current scores and busts
- Handles all endgame conditions and winner resolution
- Replay-friendly structure for multiple game sessions

---

## 💻 Technologies Used

- Python 
- `random` module for dice simulation
- Terminal-based user interaction
- Loops, functions, conditionals, and input validation

