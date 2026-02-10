# 🐍 Snake Game

A classic **Snake Game** built with Python's `turtle` graphics module — featuring colorful visuals, dynamic speed scaling, persistent high scores, and multiple food types.

## 🎮 Demo

https://github.com/DharmikMangukiya/Snake-Game/blob/main/Result/Snake_game_demo.mp4

> **📁 The full gameplay video is available in the [`Result/`](Result/) folder.**

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Dark Theme UI** | Sleek dark navy-blue background with neon-green snake |
| 👀 **Snake Eyes** | Animated eyes on the snake head that follow its direction |
| 🍎 **Multi-Type Food** | Three food types — Red (1 pt), Orange (2 pts), Gold (3 pts) — with weighted rarity |
| ⚡ **Dynamic Speed** | Game speed increases every 5 points for a progressive challenge |
| 🏆 **High Score Persistence** | Best score is saved to `high_score.txt` and persists across sessions |
| ⏸️ **Pause / Resume** | Press `P` or `Space` to pause and resume anytime |
| 🔄 **Instant Restart** | Press `R` to restart without closing the window |
| 🛡️ **Smart Food Spawning** | Food never spawns on the snake's body |

## 📂 Project Structure

```
Snake Python GAME/
├── main.py           # Game loop, screen setup, key bindings & collision detection
├── snake.py          # Snake class — movement, eyes, growth & reset logic
├── food.py           # Food class — random spawning with multiple types & point values
├── scoreboard.py     # Scoreboard class — score tracking, high score save/load, game over UI
├── high_score.txt    # Persistent high score storage
└── Result/
    └── Snake Game.mp4   # Gameplay demo video
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** (Python's `turtle` module is included in the standard library — no extra packages needed)

### Run the Game

```bash
git clone https://github.com/<your-username>/Snake-Game.git
cd Snake-Game
python main.py
```

## 🕹️ Controls

| Key | Action |
|---|---|
| `↑` `W` | Move Up |
| `↓` `S` | Move Down |
| `←` `A` | Move Left |
| `→` `D` | Move Right |
| `P` / `Space` | Pause / Resume |
| `R` | Restart Game |
| `Q` | Quit Game |

## 🏗️ How It Works

### 1. Game Loop (`main.py`)

The game runs a continuous `while True` loop that:

1. **Updates the screen** on every frame (`screen.tracer(0)` + `screen.update()` for smooth rendering).
2. **Moves the snake** forward by one grid step (20 px) each tick.
3. **Checks for collisions** — food, walls, and the snake's own tail.
4. **Adjusts speed** dynamically based on the current score.

### 2. Snake (`snake.py`)

- Starts with **3 segments** at the center of the screen.
- The head is bright **lime green** (`#00FF00`) with two small **white eyes** that rotate based on the snake's heading.
- Each `move()` call shifts every body segment forward to the position of the segment ahead of it, then advances the head.
- `extend()` adds a new segment at the tail's last position when food is eaten.
- Direction-locking prevents the snake from reversing into itself (e.g., pressing Down while going Up is ignored).

### 3. Food (`food.py`)

- Three food tiers with **weighted random selection**:
  - 🔴 **Red** — 70% chance, worth 1 point
  - 🟠 **Orange** — 25% chance, worth 2 points
  - 🟡 **Gold** — 5% chance, worth 3 points
- `refresh()` picks a random grid-aligned position and ensures it doesn't overlap with any snake segment.

### 4. Scoreboard (`scoreboard.py`)

- Displays `Score` and `Best` at the top of the screen in bright green.
- When the score exceeds the high score, it updates in real-time and **saves to `high_score.txt`** immediately.
- On **Game Over**, a red "GAME OVER" message appears with restart/quit instructions.

### 5. Dynamic Speed

The game starts at **0.1 s/frame** and gets faster by `0.005 s` for every 5 points scored, capped at a minimum of **0.03 s/frame** — keeping the game challenging as your score grows.

## 🛠️ Built With

- **Python 3** — Core language
- **Turtle Graphics** — Built-in Python module for rendering



> ⭐ If you enjoyed this project, consider giving it a star on GitHub!
