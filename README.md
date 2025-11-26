Phishing URL Detection using Random Forest & ANN
A Machine Learning project that detects whether a given URL is legitimate or phishing by extracting structural and lexical features.
This project includes:

1. Feature extraction module
2. Trained Random Forest & ANN models
3. Streamlit web application for real-time URL prediction

Features
1. Detects suspicious and phishing URLs
2. Uses Random Forest and Artificial Neural Network (ANN)
3. Extracts lexical & structural features from URLs
4. Easy-to-use Streamlit UI
5. Models trained and saved using Pickle

Dataset
The dataset used for training is:
phishing.csv from kaggle
Contains extracted lexical/structural features
Label column: status (1 = phishing, 0 = legitimate)

Execution:
Download the folder.
Make sure your system has streamlit installed 
Open terminal and locate the aapp.py file
Run the command : streamlit run app.py

