# Module 05 Overview

**Purpose**: Extend integration from one variable to multiple variables, develop the change-of-variables formula, and build the integration machinery needed to work with multivariate probability densities.

| Unit | Title | Time |
|---|---|---|
| [01](unit-01-double-integrals) | Double Integrals & Fubini's Theorem | 55–65 min |
| [02](unit-02-change-of-variables) | Change of Variables & the Jacobian Determinant | 60–70 min |
| [03](unit-03-integration-and-probability) | Integration over $\mathbb{R}^n$ & Probability Densities | 55–65 min |

## Module Learning Objectives

- Define the double integral as a limit of Riemann sums and evaluate it as an iterated integral via Fubini's theorem
- Reverse integration order to simplify evaluation over non-rectangular regions
- State the change-of-variables formula and identify $|\det(\boldsymbol{J})|$ as the local area scaling factor
- Apply polar and spherical coordinates as the canonical change of variables for Gaussian integrals
- Derive the Gaussian normalization constant $\sqrt{2\pi}$ via the polar substitution trick
- Compute marginals, expectations, and covariances as iterated integrals over joint densities

## Statistical Bridges in This Module

| Unit | Bridge | Thread |
|---|---|---|
| 01 | Joint probability densities — computing marginals via iterated integration | `[PD]` |
| 02 | Gaussian normalization integral $\int e^{-x^2/2}\,dx = \sqrt{2\pi}$ via polar substitution | `[PD]` |
| 03 | Expectation and covariance from a bivariate normal density as double integrals | `[PD]` · `[BAY]` |

## Prerequisites

This module requires fluency with single-variable integration (antiderivatives, substitution, definite integrals) from Module 00 Unit 03. The change-of-variables formula in Unit 02 uses the Jacobian from Module 03 Unit 03 in a new role — the connection is made explicit. Unit 03 assumes basic familiarity with probability densities; the Basic Probability refresher is available at `refreshers/basic-probability/`.
