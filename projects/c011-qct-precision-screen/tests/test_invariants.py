import numpy as np

from qct_reliability.core import assert_monotone, decomposition, greedy_allocate, half_up_3


def test_half_up_poverty_rounding():
    assert half_up_3(1, 16) == 0.063


def test_screen_monotonicity():
    loose = np.array([True, True, False])
    tight = np.array([True, False, False])
    assert_monotone(loose, tight)


def test_skip_and_continue():
    got = greedy_allocate([1, 1, 1], [3, 2, 1], [11, 5, 2], 50)
    assert got.cap == 10
    assert got.designated.tolist() == [False, True, True]


def test_decomposition_partition_and_nonlocal_invariant():
    parts = decomposition(
        q100=[1, 1, 1, 0, 0], q050=[0, 0, 0, 1, 1],
        e050=[0, 1, 1, 1, 1], screen_changed=[1, 1, 0, 1, 0],
    )
    assert {k: int(v.sum()) for k, v in parts.items()} == {"L1": 1, "L2": 1, "L3": 1, "G1": 1, "G2": 1}
