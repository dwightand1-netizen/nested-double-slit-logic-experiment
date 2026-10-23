# The Nested Double-Slit Logic Experiment

**Status: preliminary open research proposal — not peer reviewed.** This repository is a starting point for discussion, modeling, and collaboration. It does not report a completed experiment or a new physical discovery.

## Overview

This project explores a sequence of interferometric stages in which coherent quantum evolution alternates with measurement and classical, record-controlled feedback. The motivating question is how interference, measurement disturbance, and feedback should be distinguished when discussing logical consistency in quantum experiments.

The phrase “nested double-slit” is a working description, not a claim that this architecture is novel. Related established areas include quantum measurement, quantum erasure, sequential-measurement contextuality, quantum control, and Leggett–Garg tests.

## Research question

Can a carefully specified sequence of coherent evolution, measurement, and outcome-dependent control distinguish quantum predictions from an explicitly defined classical or macrorealist model, while avoiding the mistaken inference that quantum superposition violates the law of non-contradiction?

## Contents

- `proposal.md` — motivation, model outline, hypotheses, and proposed tests.
- `simulation.py` — idealized two-path demonstration of interference versus path-distinguishing measurement.
- `references.md` — selected starting references.
- `LICENSE` — MIT license for code.

## Run the baseline simulation

Requires Python 3.9+ and NumPy.

```bash
python -m pip install numpy
python simulation.py --shots 10000 --seed 7
```

The simulation compares an ideal coherent two-path interferometer with a path-marked case where which-path information removes the interference term. It is an explanatory baseline, not a simulation of the full nested-feedback proposal and not a test of contextuality or the law of non-contradiction.

## Important scientific cautions

- Superposition is not, by itself, a proposition being both true and false.
- The classical law of non-contradiction should not be treated as experimentally refuted by observing interference.
- Contextuality and temporal-correlation tests require operational definitions and explicit assumptions.
- Measurement can disturb a system; correlations from different measurement schedules cannot be casually combined.
- Any claimed novelty must be checked against prior literature, and predictions should be compared with standard quantum mechanics before interpreting results.

## How to contribute

Open an issue or pull request with a precise operational proposal, derivation, reproducible simulation, or relevant literature. Please state assumptions, measurement settings, expected outcomes, and how the proposal differs from established work.

## Citation and reuse

The proposal is exploratory and may change. Code is MIT-licensed. Proposal text is offered under CC BY 4.0; attribution is appreciated.
