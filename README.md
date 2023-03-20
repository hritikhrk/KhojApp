
# KHOJ -Find Missing Person

Recognize the faces and find the matching faces with missing persons. ✨

## Functionality Supported

- Register for missing person.
- Add missing person photo.
- View Matched faces reports of all founded missing-persons.

## Built Using

 - [OpenCV]() - Open Source Computer Vision and Machine Learning software library
 - [Dlib]() - C++ Library containing Machine Learning Algorithms
 - [face_recognition]() - by Adam Geitgey
 - [Flask]() - Python framework for web development

## How to install and test the app
  - Clone the repo using the cmd `git clone https://github.com/hritikhrk/KhojApp.git`
  - Go to the root directory of this repository.
  - Install virtual environment using - 
    - For Windows : `py -3 -m venv venv`
    - For Linux/MacOS: `python3 -m venv venv`
  - Activate the virtual environment using the cmd - 
    - For Windows : `venv\Scripts\activate`
    - For Linux/MacOS: `. venv/bin/activate`
  - Install all the modules and packages using the cmd `pip install -r requirements.txt`
  - Now you can run the application using `flask run`



## Face Detection

- Dlib's HOG facial detector.

## Facial Landmark Detection

- Dlib's 68 point shape predictor

## Extraction of Facial Embeddings

- face_recognition by Adam Geitgey

## Classification of Unknown Embedding

- using a Linear SVM (scikit-learn)
- The application was tested on data from 20 Person


## Screenshots

### Simple App UI



## Scope of the project 🚀





