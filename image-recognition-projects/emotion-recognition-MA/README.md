# Facial Emotion Recognition Using Convolutional Neural Network!
*PL: Rozpoznawanie emocji twarzy z wykorzystaniem konwolucyjnych sieci neuronowych*

### DATASET
FER2013 (ang. Facial Expression Recognition 2013 Dataset)

<img width="464" alt="image" src="https://user-images.githubusercontent.com/38349049/227540307-67c5c037-1a5d-4618-afe9-e1ec12784669.png">

- training set (28,709 photos)
- test set (7,178 photos)

<img width="407" alt="image" src="https://user-images.githubusercontent.com/38349049/227540866-19c24f9c-3611-431f-b834-fe9e0501c1a7.png">

### PROBLEMS:
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

### MODEL:
- CNN
- 
### DATA PREPOCESSING:
Data Augmentation with ImageDataGenerator (Keras)
- batch_size 128 - number of examples used in one iteration of model training
- one-hot encoding - converts categorical data to a binary matrix
- grayscale


### REAL TIME TESTING
OpenCV

<img width="402" alt="image" src="https://user-images.githubusercontent.com/38349049/227548325-5fcabd4e-4ce9-449a-9a14-e6c6eab3b68d.png">

<img width="454" alt="image" src="https://user-images.githubusercontent.com/38349049/227548310-33d9bdbf-f1d1-48fc-a093-8ae56ec96fac.png">


## RESULTS:
- As for the possible use cases of the emotion recognition problem, the model could be limited to only the best recognized labels, 
or to a more general division of emotions into categories: positive, neutral or negative.

