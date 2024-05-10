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

## Description

#### Block Diagram of the System
![system block](https://github.com/Samiikshyaa/NepaliHandwrittenCharacterRecognition/assets/98102213/b032d5f3-3c12-4ecb-bcdb-47d0dfd715be)


### Implementation Process

#### Data Set
(https://www.kaggle.com/datasets/rishianand/devanagari-character-set/data) is a dataset of Devanagari Script Characters. It comprises 92000 images [32x32 px] corresponding to 46 characters, consonants "ka" to "gya", and the digits 0 to 9. The vowels are missing. The CSV file is of the dimension 92000 * 1025. There are 1024 input features of pixel values in grayscale (0 to 255). 
