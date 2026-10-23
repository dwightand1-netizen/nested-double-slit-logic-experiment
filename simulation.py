"""Baseline simulation for the Nested Double-Slit Logic Experiment.

Requires Python 3.9+ and NumPy. This is not a test of the law of
non-contradiction and does not implement a contextuality inequality.
"""
import argparse
import math
import numpy as np


def p0_coherent(phi1: float, phi2: float) -> float:
    """Ideal coherent-chain output-0 probability."""
    return math.cos((phi1 + phi2) / 2.0) ** 2


def p0_after_path_measurement(phi1: float, phi2_A: float, phi2_B: float) -> float:
    """Ideal output-0 probability after path dephasing and phase-only feedback."""
    return 0.5


def sample(p0: float, shots: int, rng: np.random.Generator):
    n0 = int(rng.binomial(shots, p0))
    return n0, shots - n0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shots", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    if args.shots < 1:
        parser.error("--shots must be at least 1")

    rng = np.random.default_rng(args.seed)
    cases = [(0, 0), (math.pi/2, 0), (math.pi, 0), (math.pi/2, math.pi/2)]
    print("Baseline predictions (standard quantum mechanics)")
    print(f"shots per condition={args.shots}, seed={args.seed}")
    print("phi1/pi phi2/pi | theory coherent | theory measured | sampled coherent 0/1 | sampled measured 0/1")
    for a, b in cases:
        pc = p0_coherent(a, b)
        pm = p0_after_path_measurement(a, b, b)
        c0, c1 = sample(pc, args.shots, rng)
        m0, m1 = sample(pm, args.shots, rng)
        print(f"{a/math.pi:7.2f} {b/math.pi:7.2f} | {pc:15.4f} | {pm:14.4f} | "
              f"{c0:6d}/{c1:<6d} | {m0:6d}/{m1:<6d}")
    print("\nThis difference is predicted by standard quantum mechanics; it does not")
    print("by itself test or refute the law of non-contradiction.")


if __name__ == "__main__":
    main()
