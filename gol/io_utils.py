from __future__ import annotations
import numpy as np
from pathlib import Path


def write_states_csv(states: list[np.ndarray], out_path: str | Path) -> None:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        for k, grid in enumerate(states):
            n, m = grid.shape
            f.write(f"iter,{k}\n")
            for i in range(n):
                row = ",".join(str(int(x)) for x in grid[i, :])
                f.write(row + "\n")
            f.write("\n") 


def read_states_csv(path: str | Path) -> list[np.ndarray]:
    """
    Helper for debugging/tests if you want to load back.
    """
    path = Path(path)
    states: list[np.ndarray] = []

    with path.open("r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]

    idx = 0
    while idx < len(lines):
        if lines[idx] == "":
            idx += 1
            continue

        header = lines[idx].split(",")
        if len(header) != 2 or header[0] != "iter":
            raise ValueError(f"Bad header line: {lines[idx]}")
        idx += 1

        rows = []
        while idx < len(lines) and lines[idx] != "":
            rows.append([int(x) for x in lines[idx].split(",") if x != ""])
            idx += 1

        if not rows:
            raise ValueError("Empty grid block in CSV.")

        grid = np.array(rows, dtype=np.uint8)
        states.append(grid)
        idx += 1  

    return states
