# Credit Card Fraud Detection

A Machine Learning project that detects potentially fraudulent credit card transactions using classification algorithms.

## Project Overview

Credit card fraud is a highly imbalanced classification problem because fraudulent transactions are much less common than legitimate transactions.

This project uses historical transaction data to train machine learning models that classify transactions as:

* `0` → Normal transaction
* `1` → Fraudulent transaction

## Dataset

The dataset contains **284,807 transactions** and **31 columns**.

Features include:

* `Time`
* `V1` to `V28`
* `Amount`
* `Class`

The target variable is `Class`.

### Class Distribution

* Normal transactions: `284,315`
* Fraudulent transactions: `492`

Because fraud represents a very small portion of the dataset, accuracy alone is not a sufficient evaluation metric.

## Machine Learning Models

The following models were tested:

1. Logistic Regression
2. Random Forest
3. XGBoost

### Results

| Model               | Precision | Recall | F1-Score |
| ------------------- | --------: | -----: | -------: |
| Logistic Regression |      0.06 |   0.92 |     0.10 |
| Random Forest       |      0.91 |   0.79 |     0.84 |
| XGBoost             |      0.90 |   0.80 |     0.84 |

Random Forest and XGBoost produced similar F1-scores on the test set.

## Data Preprocessing

The following steps were performed:

* Loaded the CSV dataset using Pandas
* Separated fe
