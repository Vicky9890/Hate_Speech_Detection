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


st.set_page_config(
    page_title="Hate Speech Detector",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.markdown("""
    <style>
        .main {
            background-color: rgb(137, 137, 137);
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            color: rgb(89, 0, 255);
            font-weight: bold;
            margin-bottom: 0.2em;
        }
        .subtitle {
            text-align: center;
            color: rgb(255, 255, 255);
            font-size: 1.1em;
            margin-bottom: 2em;
        }
        div.stButton > button:first-child {
            display: block;
            margin: 0 auto;
            transition: all 0.2s ease;
        }
        
        .result-box {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 1.4em;
            font-weight: bold;
            margin-top: 20px;
        }
        .hate {
            background-color: #d90429;
        }
        .offensive {
            background-color: #ffba08;
            color: black;
        }
        .not-hate {
            background-color: #06d6a0;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'>Hate Speech Detection</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Identify whether a text contains hate speech, offensive language or Normal.</div>", unsafe_allow_html=True)


select = st.text_area("Enter a sentence or paragraph below:", height=120, placeholder="Type something like: 'I love everyone equally!'")


def cleaning(text):
    text = str(text).lower()
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("\[.*?\]", "", text)
    text = re.sub("<.*?>", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = re.sub("rt", "", text)

    stopword = set(stopwords.words("english"))
    text = " ".join([word for word in text.split() if word not in stopword])

    stemming = nltk.SnowballStemmer("english")
    text = " ".join([stemming.stem(word) for word in text.split()])

    return text


cv = CountVectorizer()
dt = DecisionTreeClassifier()

X = cv.fit_transform(cleandata)
dt.fit(X, tweetdata)


if st.button("Analyze Text"):
    if not select.strip():
        st.warning(" Please enter a sentence first.")
    else:
        clean_text = cleaning(select)
        transformed_text = cv.transform([clean_text]).toarray()
        pred = dt.predict(transformed_text)[0]  # get string value

        if pred == "Hate Speech":
            st.markdown("<div class='result-box hate'> Hate Speech Detected</div>", unsafe_allow_html=True)
        elif pred == "Offensive Language":
            st.markdown("<div class='result-box offensive'> Offensive Language</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box not-hate'> Not Hate Speech</div>", unsafe_allow_html=True)
