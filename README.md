A simple Asteroids clone made in Python with pygame.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## How to run

### With uv (recommended)

```bash
git clone <your-repo-url>
cd juguete
uv sync
uv run main.py
```

### With pip

```bash
git clone <your-repo-url>
cd juguete
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install pygame==2.6.1
python main.py
```

## Controls

| Key   | Action         |
|-------|----------------|
| W     | Move forward   |
| S     | Move backward  |
| A     | Rotate left    |
| D     | Rotate right   |
| Space | Shoot          |

Shoot the asteroids to split them. If an asteroid hits you, it's game over.

## Notes

Running the game creates `game_state.jsonl` and `game_events.jsonl` log files in the project folder.
