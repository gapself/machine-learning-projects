# Facial Emotion Recognition Using Convolutional Neural Network (CNN)

This repository contains code and resources for building a Facial Emotion Recognition system using Convolutional Neural Networks (CNN). The project utilizes the FER2013 dataset, which includes images of faces labeled with various emotional expressions.

## Table of Contents

1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Model Architecture](#model-architecture)
4. [Evaluation](#evaluation)
5. [Real time test](#real-time-test)


## Overview

Facial Emotion Recognition is a computer vision task that involves detecting and classifying the emotional state of individuals from facial expressions. This project aims to develop an accurate model capable of recognizing a range of emotions, including happiness, sadness, anger, surprise, fear, disgust, and neutrality.

## Dataset

The project uses the **FER2013** dataset, which consists of over 30,000 grayscale images of faces categorized into seven emotions. The dataset is split into training and testing sets, making it suitable for training and evaluating emotion recognition models.

<img width="464" alt="image" src="https://user-images.githubusercontent.com/38349049/227540307-67c5c037-1a5d-4618-afe9-e1ec12784669.png">

- training set (28,709 photos)
- test set (7,178 photos)

<img width="407" alt="image" src="https://user-images.githubusercontent.com/38349049/227540866-19c24f9c-3611-431f-b834-fe9e0501c1a7.png">

#### PROBLEMS:
- **IMBALANCED DATA** - In the FER2013 data set, the "happy" class can be considered the dominant class, as it contains the most data (majority class).
In turn, the smallest number of examples is in the "disgust" class, which accounts for 5.5% of the entire data set, which means
that the imbalance for this class is in the range of 1-20% and is considered to be moderate imbalance.
- **POOR QUALITY DATA** - As you can see, the collection presents photos of various shots of the human face, although there are also pictures with characters from
cartoons or robots.
There were also photos of faces obscured by hands or glasses, and photos that were too close-up.
appeared
out of focus, poorly lit, photos with different backgrounds.
In addition, stock photos with face watermarks from paid online libraries have been spotted.
The issue of incorrect labeling of some photos should also not be overlooked.
These observations may make the classification of emotions much more difficult, although it is also worth remembering that controlled differentiation of data is conducive to training neural networks.
This means that a too "simple" and ill-considered data set may lead to a situation where neural networks start to associate simple features of the input data with one specific label.
If the set of emotions representing sadness consisted only of photos of faces against a dark background, and the other categories were assigned photos against a light background, 
the network would start to associate photos against a dark background mainly with the emotion of sadness.
This would lead to misclassification of the remaining images and vice versa!

## Model Architecture

The model architecture used for this project is a Convolutional Neural Network (CNN) designed for image classification. It includes convolutional layers, pooling layers, and fully connected layers for feature extraction and classification. The specific architecture details can be found in the project code.

## Evaluation

#### DATA PREPOCESSING:
Data Augmentation with ImageDataGenerator (Keras)
- batch_size 128 - number of examples used in one iteration of model training
- one-hot encoding - converts categorical data to a binary matrix
- grayscale

#### RESULTS:
- accuracy at ~ 66%
- As for the possible use cases of the emotion recognition problem, the model could be limited to only the best recognized labels, 
or to a more general division of emotions into categories: positive, neutral or negative.
- It must be admitted that the results obtained are average, but the experts in the field of machine learning themselves achieved a test accuracy result of only 75.2% on the FER2013 dataset.

#### IMPROVEMENT: 
- Re-cleaning of data before processing: correcting incorrectly assigned labels, deleting photos
non-human images, and the removal of images that are difficult to classify by both human and machine.
- Enrichment of filtered FER2013 data with other photos (more demanding).
- Finding a more suitable model, not necessarily CNN (TO DO)
- no more one-hot encoding? https://medium.com/@kaoningyu/dont-use-one-hot-encoding-anymore-25b5882e533f


## Real Time Test
- OpenCV

install main modules package: 
```
pip install opencv-python
```
<img width="402" alt="image" src="https://user-images.githubusercontent.com/38349049/227548325-5fcabd4e-4ce9-449a-9a14-e6c6eab3b68d.png">

<img width="454" alt="image" src="https://user-images.githubusercontent.com/38349049/227548310-33d9bdbf-f1d1-48fc-a093-8ae56ec96fac.png">



### INSPIRATIONS:
😬😬😬 https://hume.ai/products/facial-expression-model
