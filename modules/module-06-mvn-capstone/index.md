# Overview

**Purpose**: Assemble every tool from Modules 01–05 into a single object — the multivariate normal distribution — and derive its properties from first principles. This is the mathematical capstone of the course.

| Unit | Title | Time |
|---|---|---|
| [01](unit-01-mvn-density) | The MVN Density — Definition & Structure | 60–70 min |
| [02](unit-02-marginals-conditionals) | Marginals, Conditionals & the Schur Complement | 65–75 min |
| [03](unit-03-mle-for-mvn) | MLE for the MVN — Putting It All Together | 60–70 min |

## Module Learning Objectives

- Write the multivariate normal density $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and interpret every factor from first principles
- Identify the geometric role of $\boldsymbol{\Sigma}$ via its eigendecomposition — level sets are ellipsoids aligned with the eigenvectors
- Derive marginal and conditional distributions by partitioning the mean vector and covariance matrix into blocks
- State the Schur complement formula and use it to compute the conditional covariance
- Derive the MLE estimators $\hat{\boldsymbol{\mu}} = \bar{\boldsymbol{x}}$ and $\hat{\boldsymbol{\Sigma}} = \frac{1}{n}\sum(\boldsymbol{x}_i - \bar{\boldsymbol{x}})(\boldsymbol{x}_i - \bar{\boldsymbol{x}})^{\top}$ by differentiating the log-likelihood
- Connect the Fisher information matrix to the precision matrix $\boldsymbol{\Sigma}^{-1}$

## Statistical Bridges in This Module

| Unit | Bridge | Thread |
|---|---|---|
| 01 | Interpreting $\boldsymbol{\Sigma}$ in a fitted Gaussian model | `[PD]` |
| 02 | Bayesian updating — Gaussian posterior as a conditional MVN | `[BAY]` |
| 03 | MLE of $(\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Sigma}})$ on a real dataset; Fisher information | `[MLE]` · `[BAY]` |

## Tools Used from Prior Modules

| Tool | Module | Where used in Module 06 |
|---|---|---|
| Quadratic forms | 00 | The exponent $(\boldsymbol{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ |
| Eigenvalues & PSD matrices | 04 | $\boldsymbol{\Sigma}$ must be PSD; level sets via eigendecomposition |
| Gradient of log-likelihood | 03 | MLE derivation in Unit 03 |
| Gaussian normalization constant | 05 | $(2\pi)^{n/2}|\boldsymbol{\Sigma}|^{1/2}$ in the denominator |
| Hessian & Fisher information | 04 | Confirming MLE is a maximum; precision matrix |
| Iterated integration | 05 | Marginals derived by integrating over partitioned components |
| Bivariate normal density | 05 | Unit 01 reduces to this and verifies the general formula |

## Prerequisites

This module assumes fluency with all of Modules 00–05. In particular: quadratic forms and matrix definiteness (Module 04 Unit 02), the Gaussian normalization constant (Module 05 Unit 02), and the bivariate normal density (Module 05 Unit 03). If any of these feel uncertain, return to the relevant unit before proceeding.
