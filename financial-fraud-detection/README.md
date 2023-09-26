# Financial Fraud Detection Project

## Overview

This project focuses on the development and evaluation of machine learning models for financial fraud detection. In particular, we have employed Logistic Regression and Random Forest algorithms to identify fraudulent transactions within a given dataset. Financial fraud detection is vital in protecting financial systems and users from malicious activities.

## Dataset

https://www.kaggle.com/datasets/ealaxi/paysim1

## Preprocessing

It's highly imbalanced data, we have more isFraud=1 than isFraud=0.

Check possible transactions types: 
```
array(['CASH_OUT', 'PAYMENT', 'CASH_IN', 'TRANSFER', 'DEBIT'],
      dtype=object)
```

Capture if money moved out of the origin account: we create new col=isMovement, where 1 is for transactions types like: CASH_OUT & TRANSFER.
```
df['isMovement'] = 0
df['isMovement'][df['type'].isin(['CASH_OUT', 'TRANSFER'])]=1
```

Create another col to check if the transaction is payment.
```
df['isPayment'] = 0
df['isPayment'][df['type'].isin(['PAYMENT', 'DEBIT'])]=1
```

In the case of financial fraud, another key factor to investigate would be the difference in the value of the source and target accounts (target accounts with significantly different values may be suspected of fraud).
```
df['accountDiff'] = abs(df['oldbalanceOrg'] - df['oldbalanceDest'])
```

## Model

1. Logistic Regression
    - Has its strengths but it may not capture complex, non-linear fraud patterns as effectively as more complex models like Random Forest or Gradient Boosting.
    - Since sklearn‘s Logistic Regression implementation uses Regularization, we need to scale our feature data. We use StandardScaler. If you plan to use the same dataset with other machine learning algorithms that do require feature scaling (e.g., logistic regression, support vector machines), you may choose to scale the features consistently across all models for consistency in data preprocessing.

2. Random Trees:
    - Random Forest's ability to handle complex, imbalanced data, provide feature importance insights, and maintain model robustness makes it a strong choice for financial fraud detection.

## Results

1. Logistic Regression
<img width="474" alt="Zrzut ekranu 2023-09-26 o 21 58 56" src="https://github.com/gapself/machine-learning-projects/assets/38349049/a01af3dd-b6cd-443c-9d31-0126622cb8cd">

2. Random Trees
<img width="476" alt="Zrzut ekranu 2023-09-26 o 21 59 35" src="https://github.com/gapself/machine-learning-projects/assets/38349049/56c65819-4823-47e5-b8c5-6dce15318796">

