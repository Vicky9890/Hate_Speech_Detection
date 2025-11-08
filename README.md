# 🧠 Hate Speech Detection Application

A **Streamlit-based web application** that detects whether a given text contains **hate speech**, **offensive language**, or **clean content (Not hate)** using a **Decision Tree Classifier** trained on labeled tweet data.

---

## 🚀 Overview

This project demonstrates a simple yet effective **Natural Language Processing (NLP)** pipeline for classifying text as *Hate Speech*, *Offensive Language*, or *Not Hate Speech*.
The app allows users to input any text, which is then cleaned, processed, and classified using a trained **Decision Tree** model.

It includes a visually appealing **Streamlit interface** with color-coded results for easy interpretation.

🔗 **Want to try it out? Visit the live app here:**  
👉 [https://hatespeechdetection-vikash.streamlit.app](https://hatespeechdetection-vikash.streamlit.app/)  

---

## 🧩 Features

- 🧼 **Text Preprocessing:** URL removal, punctuation cleaning, stopword filtering, and stemming.
- 💬 **Real-Time Prediction:** Classifies input text instantly when submitted.
- 🎨 **Custom UI Styling:** Styled using HTML and CSS for a clean and modern look.
- 📊 **Model Training & Evaluation:** Decision Tree Classifier trained using `CountVectorizer` features.
- 💾 **Pickle Integration:** Uses preprocessed data and trained model stored as `.pkl` files.

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/hate-speech-detection.git
cd hate-speech-detection
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3. Install required dependencies
Create a `requirements.txt` file with the following:
```txt
streamlit
nltk
scikit-learn
pandas
numpy
matplotlib
seaborn
```

Then install them:
```bash
pip install -r requirements.txt
```

### 4. Download NLTK stopwords
```bash
python -m nltk.downloader stopwords
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🧠 Model Details

- **Vectorizer:** `CountVectorizer()`
- **Algorithm:** `DecisionTreeClassifier()`
- **Training Data:** Preprocessed tweets labeled as  
  - *Hate Speech*  
  - *Offensive Language*  
  - *Not Hate Speech*

The model is trained on cleaned text data (`clean_data.pkl`) and label data (`dataset.pkl`).

---

## 🧹 Text Cleaning Steps

The `cleaning()` function performs several preprocessing steps:
1. Lowercasing  
2. Removing URLs, HTML tags, mentions, digits, and punctuation  
3. Removing stopwords  
4. Stemming words using `SnowballStemmer`

---

## 🖥️ User Interface

### 🔹 Normal View:
<img width="947" height="643" alt="image" src="https://github.com/user-attachments/assets/93e93351-683f-4845-9284-100004171647" />

### 🔹 Offensive:
<img width="948" height="849" alt="image" src="https://github.com/user-attachments/assets/14d7e145-1614-4492-8497-b0a33ba6e06f" />

### 🔹 Not hate sentence:
<img width="943" height="733" alt="image" src="https://github.com/user-attachments/assets/eac50512-adf1-445e-8960-fa2079c5a52b" />

### 🔹 Hate sentence:
<img width="940" height="807" alt="image" src="https://github.com/user-attachments/assets/ee336efa-13a9-4287-a77c-fe8588a938d8" />

---

## 🧑‍💻 Technologies Used

| Category | Tools/Libraries |
|-----------|----------------|
| Frontend UI | Streamlit, HTML, CSS |
| NLP | NLTK |
| ML | scikit-learn |
| Data Handling | pandas, numpy |
| Visualization | matplotlib, seaborn |

---

## 🏁 Future Improvements

- 🔍 Integrate advanced models like **Logistic Regression**, **Random Forest**, or **BERT**.  
- 🗣️ Add multilingual support for hate speech detection.  
- 📊 Include data visualization dashboards for model insights.


