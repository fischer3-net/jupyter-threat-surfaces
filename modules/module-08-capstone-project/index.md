# Overview

**Purpose**: Apply every tool built in Modules 00–07 to a single end-to-end problem — Bayesian logistic regression via variational inference. This module is a project, not a sequence of teaching topics. Each unit is a phase of a single coherent derivation and implementation.

| Unit | Phase | Time |
|---|---|---|
| [01](unit-01-problem-setup) | Problem Setup & Probabilistic Model | 55–65 min |
| [02](unit-02-variational-inference) | Variational Inference — Derivation & Implementation | 70–80 min |
| [03](unit-03-posterior-analysis) | Posterior Analysis & Course Retrospective | 60–70 min |

## What This Module Builds

A complete Bayesian logistic classifier on the Iris dataset (Setosa vs Versicolor, two features) derived and implemented from first principles:

- **Prior**: $\boldsymbol{w} \sim \mathcal{N}(\boldsymbol{0}, \sigma_0^2 \boldsymbol{I})$ — a Gaussian prior on classifier weights
- **Likelihood**: $y_i \mid \boldsymbol{w}, \boldsymbol{x}_i \sim \text{Bernoulli}(\sigma(\boldsymbol{w}^{\top}\boldsymbol{x}_i))$ — the logistic regression model
- **Variational posterior**: $q(\boldsymbol{w}) = \mathcal{N}(\boldsymbol{m}, \text{diag}(\boldsymbol{s}^2))$ — a mean-field Gaussian approximation
- **Objective**: maximize the ELBO via gradient ascent on $(\boldsymbol{m}, \boldsymbol{s})$
- **Output**: posterior predictive probabilities with calibrated uncertainty bands

## Tools Used from Prior Modules

| Tool | Module | Where used |
|---|---|---|
| Sigmoid and chain rule | 00 Unit 03, 02 | Likelihood gradient |
| Gradient of log-likelihood | 03 Unit 01 | ELBO expected log-likelihood gradient |
| Jacobian, chain rule on compositions | 03 Unit 03 | Reparameterization trick |
| Gradient descent / ascent | 03 Unit 02 | ELBO optimization |
| Hessian and convexity | 04 Units 01–02 | Confirming ELBO is well-behaved |
| Gaussian normalization constant | 05 Unit 02 | Prior and variational density |
| MVN density, KL divergence | 06 Units 01, 03 | KL term in ELBO |
| Score function, Stein's lemma | 07 Unit 01 | Reparameterization gradient |
| ELBO and KL structure | 07 Unit 03 | Full ELBO derivation |

## Statistical Threads Completed

| Thread | Resolution in Module 08 |
|---|---|
| `[PD]` | Posterior predictive distribution; calibration |
| `[MLE]` | MLE as a special case of VI with a flat prior |
| `[BAY]` | Full Bayesian inference via ELBO maximization |
| `[GLM]` | Logistic regression as the likelihood model |

## Prerequisites

All of Modules 00–07. Unit 01 is entirely mathematical — no code — so the derivations should be attempted by hand before reading the solutions. Units 02 and 03 implement the results from Unit 01 from scratch in Python.
