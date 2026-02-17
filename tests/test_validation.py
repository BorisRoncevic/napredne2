import numpy as np
from gol.automaton import random_grid, simulate_sequential
from gol.parallel import simulate_parallel


def test_seq_par_identical_small():
    n, m, t, seed = 20, 30, 15, 123
    initial = random_grid(n, m, seed=seed, p_alive=0.5)

    seq_states = simulate_sequential(initial, t)
    par_states = simulate_parallel(initial, t, workers=4)

    assert len(seq_states) == len(par_states)
    for k in range(len(seq_states)):
        assert np.array_equal(seq_states[k], par_states[k]), f"Mismatch at iter {k}"
