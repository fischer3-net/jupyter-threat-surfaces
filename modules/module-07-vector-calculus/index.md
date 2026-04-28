# Overview

**Purpose**: Extend the differentiation and integration machinery to vector fields — functions that assign a vector to every point in space. Develop the major theorems (Green's, Stokes', Gauss's) that unify the integration tools from Module 05, and connect vector calculus to score functions, information geometry, and variational inference.

| Unit | Title | Time |
|---|---|---|
| [01](unit-01-divergence-and-curl) | Vector Fields, Divergence & Curl | 55–65 min |
| [02](unit-02-line-integrals) | Line Integrals & Conservative Fields | 60–70 min |
| [03](unit-03-surface-integrals-and-theorems) | Surface Integrals & the Major Theorems | 65–75 min |

## Module Learning Objectives

- Define a vector field and compute its divergence and curl using the del operator $\nabla$
- Interpret divergence as a measure of net outward flow and curl as a measure of local rotation
- Compute the Laplacian $\nabla^2 f$ and identify harmonic functions
- Evaluate line integrals of scalar and vector fields over parameterized curves
- Identify conservative vector fields via the curl test and recover their potential functions
- State Green's theorem, Stokes' theorem, and the divergence theorem and identify when each applies
- Connect the score function to a vector field and derive Stein's lemma

## Statistical Bridges in This Module

| Unit | Bridge | Thread |
|---|---|---|
| 01 | Score function as a vector field; Stein's lemma $\mathbb{E}[\nabla \log p(\boldsymbol{X})] = \boldsymbol{0}$ | `[MLE]` |
| 02 | Gradient flow in optimization as a conservative field; potential = negative loss | `[MLE]` · `[GLM]` |
| 03 | Divergence theorem as the foundation of the ELBO in variational inference; KL divergence and information flow | `[BAY]` |

## Prerequisites

This module builds on the gradient and Jacobian from Module 03, the integration tools from Module 05, and the log-likelihood score function from Module 03 Unit 01 and Module 06 Unit 03. The cross product from Module 00 Unit 02 is used in Unit 01 (curl) and Unit 03 (surface normals).
