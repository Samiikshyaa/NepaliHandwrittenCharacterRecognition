# Nepali-Handwritten-Character-Recognition-Using-CNN

## Abstract
Handwritten character recognition is crucial for various applications, including
language processing and document digitization. This system focuses specifically on
Nepali handwritten character recognition, utilizing Convolutional Neural Network
(CNN) algorithms to achieve precise recognition outcomes. The methodology
involves collecting a diverse dataset of handwritten Nepali characters, organizing it
into a structured CSV format, and applying augmentation and normalization
techniques to enhance data quality. The CNN architecture, featuring convolutional
layers for feature extraction, is complemented by max-pooling layers to reduce
dimensionality and dropout layers to prevent overfitting, ensuring robust recognition
performance.
User accessibility is prioritized through two input modalities: direct image upload and
a user-friendly graphical interface. Real-time feedback mechanisms enable users to
input handwritten characters for recognition and promptly receive accurate
recognition results. Performance evaluation was evaluated employing the F1-score as a
metric. It demonstrated the system's outstanding accuracy of 98.37%.

## Requirements
1. Tensorflow
2. Flask
3. Numpy
4. Pandas
5. Matplotlib

## Description

#### Block Diagram of the System
![system block](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/b032d5f3-3c12-4ecb-bcdb-47d0dfd715be)



## Implementation Process

#### Data Set
(https://www.kaggle.com/datasets/rishianand/devanagari-character-set/data) is a dataset of Devanagari Script Characters. It comprises 92000 images [32x32 px] corresponding to 46 characters, consonants "ka" to "gya", and the digits 0 to 9. The vowels are missing. The CSV file is of the dimension 92000 * 1025. There are 1024 input features of pixel values in grayscale (0 to 255). 


![dataset sample](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/2d5dd1e0-77b9-4cfd-86d6-1930e630947c)

#### CNN-based classification
CNN Flow:

![CNN flow](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/2c9e0f56-912d-49f5-a3f6-4d7336c39ed7)

CNN Architecture:
![Architecture](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/639984ea-189b-4609-a28b-92df471bbcfd)


## Result And Analysis
#### Model Summary
![model summary](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/d43ae467-2b9f-41b5-9efa-1509dd844c4a)



#### Accuracy Vs Epoch
![AccuracyVsEpoch](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/0b06eaf7-a5b2-4f0e-ada0-873919e79d1a)



#### Loss Vs Epoch
![LossVsEpoch](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/21176cae-fd8e-49a9-b5ad-129e6cbdefa3)



## Sample Result (Real-Time Inputs)

![tha](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/19857183-2e3a-48e3-b108-069511525523)
![ka](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/21debd8e-fa59-4af2-a6ad-19dc42278540)
![ja](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/9f06b91a-faf6-4af1-8898-ce1d7cfff160)

![7](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/a22ae8ec-28bf-4451-b229-e758e90fc5bb)
![1](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/44b3c3ed-d53e-4bc4-b32e-e8cff89b9311)

![irrelavant1](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/e8d5e3d3-64d9-4eb7-af23-1e399981fac2)
![irr1](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/74d8ae9f-3715-479e-a0ee-5948aa379db2)



## User Interface
![UI](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/954ad025-676d-45f3-bbac-53b05843bd32)




A major project submitted in partial fulfillment for the requirement of the Bachelors' degree in Computer Engineering. 
