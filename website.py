import streamlit as st
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier


nltk.download('stopwords')

cleandata = pickle.load(open("clean_data.pkl", "rb"))
tweetdata = pickle.load(open("dataset.pkl", "rb"))

st.header("Hate Speech Detection")

select = st.text_input("Enter any sentence:")

def cleaning(text):
    text = str(text).lower()
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("\[.*?\]", "", text)
    text = re.sub("<.*?>", "", text)
    text = re.sub("[%s]" %re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = re.sub("rt", "", text)

    # stopwords processing
    stopword = set(stopwords.words("english"))
    text = [word for word in text.split(" ") if word not in stopword]
    text = " ".join(text)

    # stemming processing
    stemming = nltk.SnowballStemmer("english")
    text = [stemming.stem(word) for word in text.split(" ")]
    text = " ".join(text)
    
    return text

cv=CountVectorizer()
dt=DecisionTreeClassifier()

X = cv.fit_transform(cleandata)

dt.fit(X, tweetdata)



if st.button("Submit"):
    clean_text = cleaning(select)
    transformed_text = cv.transform([clean_text]).toarray()
    pred = dt.predict(transformed_text)
    
    str_name = ' '.join(pred)
    
    result =[]
    if pred == "Hate Speech":
        result = "Hate Speech"
        st.image("https://cdn.shortpixel.ai/spai/w_700+q_glossy+ret_img+to_auto/www.article19.org/wp-content/uploads/2017/11/Hate_speech_web_image.jpg")
    elif pred == "Offensive Language":
        result = "Offensive Language"  
        st.image("https://cdn.vectorstock.com/i/preview-1x/08/74/offensive-language-rubber-stamp-vector-12760874.jpg")
    else:
        result = "Not Hate Speech"
        st.image("https://www.coe.int/documents/12280688/19280137/No-Hate-Speech-Movement_350x150px.png/478b0276-092d-4cf9-9600-a676814837ac?t=1465219125000")
               
        
        
    st.write("Prediction:", result)    
        
