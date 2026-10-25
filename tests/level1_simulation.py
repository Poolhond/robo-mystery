"""Reference simulation for level 1: De energiecellen.

Run with: python3 tests/level1_simulation.py
Only Python's standard library is required.
"""
import random
import statistics

ROWS, COLS = 7, 5
COLORS = "RBGY"
TARGET = 10
START = [
    list("RYYRR"),
    list("YBYYR"),
    list("YYBRB"),
    list("BBRBR"),
    list("BRRYY"),
    list("GYBYG"),
    list("YBYRY"),
]


def matches(board):
    found = set()
    for r in range(ROWS):
        c = 0
        while c < COLS:
            end = c + 1
            while end < COLS and board[r][end] == board[r][c]:
                end += 1
            if board[r][c] and end - c >= 3:
                found.update((r, k) for k in range(c, end))
            c = end
    for c in range(COLS):
        r = 0
        while r < ROWS:
            end = r + 1
            while end < ROWS and board[end][c] == board[r][c]:
                end += 1
            if board[r][c] and end - r >= 3:
                found.update((k, c) for k in range(r, end))
            r = end
    return found


def legal_moves(board):
    moves = []
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in ((1, 0), (0, 1)):
                rr, cc = r + dr, c + dc
                if rr >= ROWS or cc >= COLS:
                    continue
                board[r][c], board[rr][cc] = board[rr][cc], board[r][c]
                valid = bool(matches(board))
                board[r][c], board[rr][cc] = board[rr][cc], board[r][c]
                if valid:
                    moves.append(((r, c), (rr, cc)))
    return moves


def refill_and_collapse(board, rng):
    gained = 0
    cascades = 0
    while True:
        found = matches(board)
        if not found:
            break
        cascades += 1
        if cascades > 100:
            raise AssertionError("Cascade safety guard reached")
        for r, c in found:
            if board[r][c] == "R":
                gained += 1
            board[r][c] = None
        for c in range(COLS):
            remaining = [board[r][c] for r in range(ROWS - 1, -1, -1)
                         if board[r][c] is not None]
            for r in range(ROWS - 1, -1, -1):
                idx = ROWS - 1 - r
                board[r][c] = remaining[idx] if idx < len(remaining) else rng.choice(COLORS)
    return gained, cascades


def reshuffle(board, rng):
    pieces = [piece for row in board for piece in row]
    for _ in range(10_000):
        rng.shuffle(pieces)
        candidate = [pieces[i:i + COLS] for i in range(0, len(pieces), COLS)]
        if not matches(candidate) and legal_moves(candidate):
            return candidate
    raise AssertionError("Could not find a valid reshuffle")


def simulate(seed):
    rng = random.Random(seed)
    board = [row[:] for row in START]
    assert not matches(board), "Start board has an automatic match"
    assert legal_moves(board), "Start board has no legal move"
    total = moves = reshuffles = 0
    while total < TARGET:
        available = legal_moves(board)
        if not available:
            board = reshuffle(board, rng)
            reshuffles += 1
            continue
        (r, c), (rr, cc) = rng.choice(available)
        board[r][c], board[rr][cc] = board[rr][cc], board[r][c]
        gained, _ = refill_and_collapse(board, rng)
        total += gained
        moves += 1
        if total < TARGET and not legal_moves(board):
            board = reshuffle(board, rng)
            reshuffles += 1
    return moves, total, reshuffles


def main():
    assert len(START) == ROWS and all(len(row) == COLS for row in START)
    assert len(matches(START)) == 0
    assert len(legal_moves(START)) == 22
    results = [simulate(seed) for seed in range(10_000)]
    moves = sorted(result[0] for result in results)
    assert all(result[1] >= TARGET for result in results)
    assert all(result[2] == 0 for result in results)
    p95 = moves[int(0.95 * len(moves)) - 1]
    print(f"Partijen: {len(results)}")
    print(f"Doel bereikt: {sum(result[1] >= TARGET for result in results)}/{len(results)}")
    print(f"Gemiddelde zetten: {statistics.mean(moves):.2f}")
    print(f"Mediaan zetten: {statistics.median(moves):.0f}")
    print(f"95e percentiel: {p95}")
    print(f"Maximum zetten: {max(moves)}")
    print(f"Totaal herschikkingen: {sum(result[2] for result in results)}")
    print(f"Startmatches: {len(matches(START))}")
    print(f"Geldige startzetten: {len(legal_moves(START))}")


if __name__ == "__main__":
    main()
