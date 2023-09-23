# Breast Cancer Classifiers Project

## Overview

This repository contains code and resources for a breast cancer classifier project. The goal of this project is to develop and evaluate machine learning models that can accurately classify breast cancer based on various features and data sources. Breast cancer is a significant health concern worldwide, and accurate classification can aid in early diagnosis and treatment planning.

## Table of Contents

1. [Project Description](#project-description)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Models](#models)
6. [Evaluation](#evaluation)
7. [Contributing](#contributing)

## Project Description

Breast cancer is a complex disease with different subtypes and variations. Machine learning techniques can help in automating the process of identifying and classifying breast cancer, which can assist medical professionals in making more accurate and timely diagnoses. This project explores various machine learning models and algorithms to classify breast cancer into different categories, such as benign or malignant.

## Dataset

The dataset used for this project is the [Breast Cancer Wisconsin (Diagnostic) Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)), which contains a collection of features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. The dataset includes various features such as mean radius, mean texture, mean smoothness, and more. It is a widely used dataset for breast cancer classification tasks.

Data is divided into train set 90 % and test set 10%. We used Stratified Validation to protect the data from random split. 
> There is something that can potentially affect the quality of your prediction that is most often forgotten when generating these splits: the distribution of your target variable(s).
> These dataset divisions are usually generated randomly according to a target variable. However, when doing so, the proportions of the target variable among the different splits can differ, especially in the case of small datasets. This means that we are training and evaluating in heterogeneous subgroups, which will lead to prediction errors.
> The solution is simple: stratified sampling. This technique consists of forcing the distribution of the target variable(s) among the different splits to be the same. This small change will result in training on the same population in which it is being evaluated, achieving better predictions.
> source: https://towardsdatascience.com/stratified-sampling-you-may-have-been-splitting-your-dataset-all-wrong-8cfdd0d32502

Number of Instances: 569
Class Distribution: 212 - Malignant, 357 - Benign

## Installation

To run the code in this repository, follow these installation steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/gapself/breast-cancer-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd breast-cancer-detection
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

## Usage

To use the classifiers developed in this project, you can refer to the provided Jupyter notebooks or Python scripts. The primary entry points are the model training and evaluation scripts.

## Models

In this project, we explore 8 various machine learning models for breast cancer classification:

- Linear Regression  👎 👎 👎
  > Purpose of using it for this project?
  > - proving that its not an accurate algorithm for classification problems
  
  > Description:
  > - used to predict the value of a variable based on the value of another variable
  > - it estimates the relationship between two quantitative variables
  > - the goal is to predict a continuous numeric output

  > Use examples:
  > - estimating income over time
  > - computing mileage rates
  > - predicting profit
  
- Gaussian Process (GaussianProcessClassifier) 👎 👎 👎
  > Description:
  > - primarily used for probabilistic binary classification tasks, providing not only point predictions but also uncertainty estimates for each prediction
  
  > Use examples:
  > - Anomaly Detection (fraud detection)
  > - Time Series Classification
  > - Medical Diagnosis
  > - Natural Language Processing
  
- Gaussian Naive Bayes (GaussianNB) 👎 👎 👎
  > GaussianNB can be used for breast cancer classification, but it may not be the best choice, especially for complex tasks like this. The main reason is that it assumes that features are normally distributed, which may not hold true for all the features in a breast cancer dataset. 

  > Description:
  > - based on Bayes' theorem and assumes that features are normally distributed within each class.
  
  > Use examples:
  > - Text Classification (spam or not)
  > - Sentiment Analysis (positive, negative, or neutral of customer reviews or social media posts)
  > - Document Categorization (topics to category)
  > - Medical Diagnosis: Identifying diseases or conditions based on patient symptoms and test results.
  > - Customer Churn Prediction: Predicting whether customers are likely to churn or stay with a service provider

- Support Vector Classification (SVC) 👍 🥳
  > Description:
  > - it is a supervised machine learning algorithm that falls under the category of support vector machines (SVMs)
  > - designed for binary classification tasks (goal is to classify data points into one of two classes: typically referred to as the positive class and the negative class)
  > - can handle non-linearly separable data by using a kernel function
  > - The goal of SVC is to find the optimal hyperplane that maximizes the margin, which is the distance between the hyperplane and the nearest data points from each class. This maximization of margin helps the model generalize well to unseen data.
  > - C parameter in SVC represents the regularization parameter. It controls the trade-off between maximizing the margin and minimizing the classification error. A smaller C value makes the margin wider but may allow some misclassification, while a larger C value reduces misclassification but may lead to a narrower margin. The choice of C depends on the specific problem and dataset.

  > Use examples:
  > - text categorization
  > - image classification
  > - medical diagnosis

- Random Forest 👍 🥳
  > Description:
  > - supervised machine learning algorithm used for both classification and regression tasks
  > - random Forest consists of multiple decision trees
  > - it selects a subset of features for each tree

  > Use examples:
  > - spam email detection
  > - sentiment analysis
  > - disease diagnosis
  > - credit risk assessment

- Multi-layer Perceptron Classifier (MLPClassifier) 👍 🥳
  > Yes, MLPClassifier can be suitable for breast cancer classification, especially when dealing with tabular data containing diagnostic features. It has the capacity to model complex relationships in the data and can adapt to non-linear patterns. However, its performance depends on factors like the architecture of the neural network, hyperparameter tuning, and the specific characteristics of the dataset. It is a common choice for medical diagnosis tasks, but its effectiveness should be evaluated in comparison to other machine learning models like logistic regression, support vector machines, or random forests.
  
  > Description:
  > - is a type of artificial neural network (ANN) specifically designed for classification tasks. It consists of multiple layers of interconnected neurons (perceptrons) and uses backpropagation to learn and make predictions.
  
  > Use examples:
  > - Image Classification (patterns)
  > - NLP
  > - Speech Recognition
  > - Credit Risk Assessment
  > - Medical Diagnosis

  
- K-Nearest Neighbors (KNeighborsClassifier) 👍 🥳
  > KNeighborsClassifier can be suitable for breast cancer classification. However, its performance depends on factors like the choice of distance metric, the number of neighbors (k), and the scaling of features. It is important to preprocess the data appropriately and choose optimal hyperparameters for the specific dataset. While it can work well for some breast cancer datasets, other machine learning algorithms like logistic regression, support vector machines, random forests, or neural networks are also commonly used for this task and should be considered for comparison.
  
  > Description:
  > - supervised machine learning algorithm used for classification tasks. It is a type of instance-based learning or lazy learning, where predictions are made based on the majority class of its k-nearest neighbors in the feature space.
  
  > Use examples:
  > - Image classification
  > - Recommendation Systems
  > - Anomaly Detection
  > - Customer Segmentation
  > - Medical Diagnosis

- Stochastic Gradient Descent Classifier (SGDClassifier) 👍 🥳
  > SGDClassifier can be used for breast cancer classification, especially when dealing with large datasets or online learning scenarios. It is effective for linear classification tasks but may require feature scaling and careful hyperparameter tuning. While it may not capture complex non-linear relationships as well as some other algorithms, it can serve as a baseline model for breast cancer classification and provide reasonable results, particularly if the dataset has linearly separable characteristics. However, its performance should be compared to other machine learning models commonly used for breast cancer classification to determine the best approach for a specific dataset.

  > Description:
  > - type of linear classifier that uses stochastic gradient descent as its optimization algorithm. It is particularly suited for large-scale and online machine learning tasks.
  
  > Use examples:
  > - Text Classification:
  > - NLP
  > - Image Classification
  > - Customer Churn Prediction
  > - Recommendation Systems

## Evaluation

We create dictionary called classifiers to apply model for every classifier. Each model is implemented and evaluated separately.
```
classifiers = {"LinearRegression" : LinearRegression(),
               "GaussianProcessClassifier" : GaussianProcessClassifier(),
               "GaussianNB" : GaussianNB(),
               "SVC" : SVC(),
               "MLPClassifier" : MLPClassifier(),
               "KNeighborsClassifier" : KNeighborsClassifier(),
               "SGDClassifier" : SGDClassifier()}
```
Our .score() results:
> SCORE - It is used to evaluate the performance of a model on a given dataset. The score method returns a value between 0 and 1, where 1 represents a perfect fit and 0 represents a complete mismatch.
> The score method is implemented differently for different classifiers. For example, in a linear regression model, the score method returns the coefficient of determination R^2 of the prediction. In a classification model, the score method returns the mean accuracy on the given test data and labels.
> source: https://saturncloud.io/blog/understanding-the-difference-between-score-and-accuracyscore-in-scikitlearn/
```
LinearRegression() 
 0.6970003216389806
GaussianProcessClassifier() 
 0.9298245614035088
GaussianNB() 
 0.9824561403508771
SVC() 
 0.9298245614035088
MLPClassifier() 
 0.8771929824561403
KNeighborsClassifier() 
 0.9122807017543859
SGDClassifier() 
 0.8596491228070176
 ```

We assess the model performance using various metrics and techniques, including cross-validation, confusion matrices, ROC curves, and AUC-ROC scores. 

<b>Cross-validation</b>
> With a small data set, it is difficult to isolate a representative test set.
> 1. One way is to run the entire process several times and report the averages and deviations of the results obtained.
> 2. A better way is to split the entire dataset into K bundles and iteratively use each bundle as test data and all others (in each iteration) as training data.
> Use the StratifiedKFold class from the sklearn.model_selection module to divide the set into 5 parts and repeat the previous experiment to calculate model accuracy. As a result, enter the average value and standard deviation for all divisions of a given model.

For all models except linear regression, apply fit methods on training data and predict methods on test data as appropriate. Then calculate the accuracy (accuracy_score), precision, sensitivity (recall), f-score and confusion matrix for individual classifiers. Also use the classification_report method to see the overall report.

<b>ROC and AUC</b>
> Use all models except linear regression and GPC, and for SVC add probability=True. Use cross-validation to train each model and calculate predict_proba for the entire set. Then calculate roc_curve and auc_score for all models and plot on the graph.

The results and conclusions are documented in the project notebooks and reports.


## Contributing

Contributions to this project are welcome. If you have any ideas, improvements, or bug fixes to suggest, please open an issue or create a pull request. Be sure to follow the [Contributing Guidelines](CONTRIBUTING.md) when submitting your contributions.

---

Thank you for your interest in the Breast Cancer Classifiers Project. If you have any questions or need assistance, please feel free to reach out to the project maintainers or contributors. Together, we can make a positive impact in the field of breast cancer diagnosis through machine learning.
