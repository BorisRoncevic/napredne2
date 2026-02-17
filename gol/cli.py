from __future__ import annotations
import argparse
import time
import numpy as np

from gol.automaton import random_grid, simulate_sequential
from gol.parallel import simulate_parallel
from gol.io_utils import write_states_csv


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="2D Conway's Game of Life (torus) - seq vs multiprocessing")
    p.add_argument("--n", type=int, required=True, help="Rows (N)")
    p.add_argument("--m", type=int, required=True, help="Cols (M)")
    p.add_argument("--t", type=int, required=True, help="Iterations (T)")
    p.add_argument("--seed", type=int, required=True, help="Random seed for initial state")
    p.add_argument("--mode", choices=["seq", "par", "both"], default="both", help="Run mode")
    p.add_argument("--workers", type=int, default=None, help="Number of worker processes for parallel mode")
    p.add_argument("--out", type=str, default="states.csv", help="Output CSV file path")
    p.add_argument("--p_alive", type=float, default=0.5, help="Initial probability of alive cells")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.n <= 0 or args.m <= 0 or args.t < 0:
        raise ValueError("N and M must be > 0, T must be >= 0")
    if not (0.0 <= args.p_alive <= 1.0):
        raise ValueError("p_alive must be in [0, 1]")

    initial = random_grid(args.n, args.m, seed=args.seed, p_alive=args.p_alive)

    if args.mode == "seq":
        t0 = time.perf_counter()
        states = simulate_sequential(initial, args.t)
        dt = time.perf_counter() - t0
        write_states_csv(states, args.out)
        print(f"[SEQ] wrote {len(states)} states to {args.out} in {dt:.4f}s")
        return 0

    if args.mode == "par":
        t0 = time.perf_counter()
        states = simulate_parallel(initial, args.t, workers=args.workers)
        dt = time.perf_counter() - t0
        write_states_csv(states, args.out)
        print(f"[PAR] workers={args.workers} wrote {len(states)} states to {args.out} in {dt:.4f}s")
        return 0

    # both: run both and validate identical
    t0 = time.perf_counter()
    seq_states = simulate_sequential(initial, args.t)
    dt_seq = time.perf_counter() - t0

    t1 = time.perf_counter()
    par_states = simulate_parallel(initial, args.t, workers=args.workers)
    dt_par = time.perf_counter() - t1

    # validation
    ok = True
    if len(seq_states) != len(par_states):
        ok = False
    else:
        for k in range(len(seq_states)):
            if not np.array_equal(seq_states[k], par_states[k]):
                ok = False
                print(f"[VALIDATION FAIL] mismatch at iter {k}")
                break

    # write the sequential by default (or you can choose)
    write_states_csv(seq_states, args.out)

    print(f"[SEQ] {dt_seq:.4f}s | [PAR workers={args.workers}] {dt_par:.4f}s | identical={ok}")
    print(f"Wrote states to {args.out}")
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
