# Box-Cox Transformation Learnings

A collection of experiments and learnings related to the Box-Cox transformation, focusing on understanding its application for data normalization and stabilization of variance. Includes Python scripts and Jupyter notebooks demonstrating the transformation's effects on different datasets.


## Contents

- **notebooks**: Jupyter notebook exploring the Box-Cox transformation on a sample real-world dataset, with step-by-step explanations.
- **scripts**: Python scripts that implement and utilize the Box-Cox transformation.
- **data**: Sample dataset used for experiment.

## Overview

The Box-Cox transformation is a family of power transformations that helps stabilize variance and make data more closely resemble a normal distribution. This repository contains hands-on exercises, including:

- Applying Box-Cox to time series data
- Visualizing the effects of the transformation

## Introduction to Box-Cox Transformation

The **Box-Cox transformation** is a family of power transformations that is used to stabilize variance and make data more closely approximate a normal distribution. The transformation is defined as:

- **If λ ≠ 0**:  
  $`y(λ) = (x^λ - 1)/λ`$

- **If λ = 0**:  
  $`y(λ) = log(x)`$

Where:
- **x** is the input data.
- **λ** (lambda) is the transformation parameter.

### Purpose and Applications
- **Variance Stabilization**: Box-Cox helps in making the variance of the data more consistent across different levels of the independent variable.
- **Normalization**: It can transform skewed data into a more normal distribution, which is often a requirement for many statistical models.
- **Improving Model Performance**: In regression models, applying the Box-Cox transformation can often improve model performance by making the relationship between the variables more linear and stabilizing variance.

The optimal value of $(\lambda)$ can be estimated by maximum likelihood estimation, and typically, a range of values is tested to find the best fit for the given dataset. When $(\lambda = 0)$, the transformation reduces to a logarithmic transformation, which is useful for handling exponential growth or data with high positive skew.

## Requirements

To run the scripts and notebooks, you'll need the following Python packages:
- numpy
- pandas
- scipy
- matplotlib
- argparse
- jupyter (for running notebooks)

Install the required packages using:
```bash
pip install -r requirements.txt
