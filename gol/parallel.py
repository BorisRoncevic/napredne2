from __future__ import annotations
import os
import numpy as np
import multiprocessing as mp


def _compute_rows(args: tuple[np.ndarray, int, int]) -> tuple[int, np.ndarray]:
    """
    Worker: compute next state for rows [row_start, row_end) inclusive-exclusive.
    Returns (row_start, chunk) where chunk has shape (row_end-row_start, M).
    """
    prev, row_start, row_end = args
    n, m = prev.shape
    out = np.zeros((row_end - row_start, m), dtype=np.uint8)

    for local_i, i in enumerate(range(row_start, row_end)):
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
                out[local_i, j] = 1 if (neighbors == 2 or neighbors == 3) else 0
            else:
                out[local_i, j] = 1 if neighbors == 3 else 0

    return row_start, out


def _split_rows(n: int, workers: int) -> list[tuple[int, int]]:
    workers = max(1, min(workers, n))
    base = n // workers
    rem = n % workers

    ranges = []
    start = 0
    for w in range(workers):
        add = base + (1 if w < rem else 0)
        end = start + add
        ranges.append((start, end))
        start = end
    return ranges


def step_torus_parallel(prev: np.ndarray, workers: int | None = None) -> np.ndarray:
    """
    Parallel version of one iteration.
    """
    n, m = prev.shape
    if workers is None:
        workers = os.cpu_count() or 1

    ranges = _split_rows(n, workers)
    tasks = [(prev, a, b) for (a, b) in ranges]

    nxt = np.zeros((n, m), dtype=np.uint8)

    with mp.Pool(processes=len(ranges)) as pool:
        results = pool.map(_compute_rows, tasks)

    for row_start, chunk in results:
        nxt[row_start:row_start + chunk.shape[0], :] = chunk

    return nxt


def simulate_parallel(initial: np.ndarray, t: int, workers: int | None = None) -> list[np.ndarray]:
    states = [initial.copy()]
    prev = initial.copy()

    for _ in range(t):
        nxt = step_torus_parallel(prev, workers=workers)
        states.append(nxt)
        prev = nxt

    return states
