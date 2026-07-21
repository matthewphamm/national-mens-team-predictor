# National Football Match Predictor

A football match outcome predictor built on Elo ratings, Poisson regression, and Monte Carlo simulation - trained and validated on 49,000+ international matches (1872-2026).

## Overview

This project predicts win/draw/loss probabilities for international football matches by:
1. Building an Elo-style strength rating for every national team from previous match results
2. Using those ratings to predict expected goals via a Poisson regression model
3. Running Monte Carlo simulation (10,000 trials per match) to convert expected goals into win/draw/loss probabilities

Two prediction methods were built and compared: a lightweight Elo-based heuristic, and a more complex Elo → Poisson regression → Monte Carlo pipeline. Both were validated using a walk-forward backtest.

## Results

| Method | Test period | Matches | Top-pick accuracy |
|---|---|---|---|
| Elo heuristic | 2010–2026 | 15,929 | **58.6%** |
| Elo → Poisson regression → Monte Carlo | 2010–2026 | 15,929 | 57.5% |

**Key finding:** the simpler Elo-based heuristic outperformed the more complex Poisson + Monte Carlo pipeline on a fair, identical test set. This is attributed to two design trade-offs made for computational practicality: the Poisson model's coefficients were trained on a single fixed split (after 2010) rather than continuously updated, while Elo ratings updated after every match throughout the entire test and the Monte Carlo simulation treats home/away goals as statistically independent, which is known to under-predict low-scoring draws.
