# Module 04 Overview

**Purpose**: Develop the tools for finding and classifying extrema of multivariable functions — unconstrained and constrained — and connect them to the optimization problems at the heart of statistical estimation.

| Unit | Title | Time |
|---|---|---|
| [01](unit-01-critical-points) | Critical Points & the Second-Derivative Test | 55–65 min |
| [02](unit-02-hessian-and-convexity) | The Hessian & Convexity | 55–65 min |
| [03](unit-03-lagrange-multipliers) | Constrained Optimization & Lagrange Multipliers | 60–70 min |

## Module Learning Objectives

- Find critical points of a multivariable function by solving $\nabla f = \boldsymbol{0}$
- Construct the Hessian matrix and use it to classify critical points as minima, maxima, or saddle points
- State the definitions of convexity and positive definiteness and explain why convex problems have unique global minima
- Apply Newton's method as a second-order alternative to gradient descent
- Derive the Ridge regression closed-form solution analytically from the gradient condition
- Set up the Lagrangian for an equality-constrained optimization problem and solve using the KKT conditions

## Statistical Bridges in This Module

| Unit | Bridge | Thread |
|---|---|---|
| 01 | Hessian of the Gaussian log-likelihood — confirming the MLE is a maximum | `[MLE]` |
| 02 | Ridge regression closed-form solution; Newton's method vs gradient descent | `[GLM]` |
| 03 | Maximum entropy distribution; Lasso as a constrained optimization problem | `[MLE]` · `[GLM]` |

## Prerequisites

This module builds on **Module 03 — The Gradient & Directional Derivatives** throughout. Unit 02 requires basic familiarity with eigenvalues and matrix definiteness; a refresher is available at `refreshers/matrix-algebra-basics/`. Unit 03 introduces new machinery (Lagrange multipliers) with no prerequisites beyond Units 01 and 02 of this module.
