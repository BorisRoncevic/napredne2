from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Config:
    n: int
    m: int
    t: int
    seed: int


def random_grid(n: int, m: int, seed: int, p_alive: float = 0.5) -> np.ndarray:
    rng = np.random.default_rng(seed)
    grid = (rng.random((n, m)) < p_alive).astype(np.uint8)
    return grid


def step_torus(prev: np.ndarray) -> np.ndarray:
    """
    Conway's Game of Life, Moore neighborhood, torus boundary (wrap-around).
    prev: uint8 matrix of shape (N, M) with 0/1.
    returns: new grid (uint8) computed from prev (double buffering concept).
    """
    n, m = prev.shape
    nxt = np.zeros_like(prev, dtype=np.uint8)

    for i in range(n):
        im1 = (i - 1) % n
        ip1 = (i + 1) % n
        for j in range(m):
            jm1 = (j - 1) % m
            jp1 = (j + 1) % m

            neighbors = (
                prev[im1, jm1] + prev[im1, j] + prev[im1, jp1] +
                prev[i, jm1]               + prev[i, jp1] +
                prev[ip1, jm1] + prev[ip1, j] + prev[ip1, jp1]
            )

            cell = prev[i, j]
            if cell == 1:
                nxt[i, j] = 1 if (neighbors == 2 or neighbors == 3) else 0
            else:
                nxt[i, j] = 1 if neighbors == 3 else 0

    return nxt


def simulate_sequential(initial: np.ndarray, t: int) -> list[np.ndarray]:
    """
    Returns list of states for each iteration including iteration 0.
    """
    states = [initial.copy()]
    prev = initial.copy()

    for _ in range(t):
        nxt = step_torus(prev)
        states.append(nxt)
        prev = nxt

    return states
