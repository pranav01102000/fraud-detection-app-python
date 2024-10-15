import streamlit as st
import warnings

warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import tweepy
import json
from tweepy import OAuthHandler
import re
import textblob
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import time



# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
import seaborn as sns
import requests

# sns.set_style('darkgrid')


df = pd.DataFrame(columns=["Date", "User", "IsVerified", "Review"])
# Security
# passlib,hashlib,bcrypt,scrypt
import hashlib


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

    # Function to Clean the Tweet.


def clean_tweet(tweet):
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([RT])', ' ', tweet.lower()).split())


def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


def prepCloud(Topic_text, Topic):
    Topic = str(Topic).lower()
    Topic = ' '.join(re.sub('([^0-9A-Za-z \t])', ' ', Topic).split())
    Topic = re.split("\s+", str(Topic))
    stopwords = set(STOPWORDS)
    stopwords.update(Topic)  ### Add our topic in Stopwords, so it doesnt appear in wordClous
    ###
    text_new = " ".join([txt for txt in Topic_text.split() if txt not in stopwords])
    return text_new


def main():
    st.title("Fraud Application Detection using Sentiment Analysis.")

    menu = ["Home", "Login", "SignUp", "Text Analysis"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("why Fraud App Detection?")
        st.markdown(
            "Most of us these days utilise Android and IOS mobile devices, and we also use the play store or app store capability on a regular basis. Both marketplaces provide a large number of applications, but unfortunately, a small number of those applications are fraudulent. Such programmes can cause phone harm and data theft. As a result, such applications must be labelled so that store users can identify them. As a result, we propose a web application that will process the information, comments, and application evaluation. As a result, it will be easy to determine if an application is fraudulent or not.")
        st.image("sentiment.png", width=700)
    elif choice == "Text Analysis":
        st.subheader("Text Analysis")
        data = str()
        data = str(st.text_input("Enter the Comment to analyze sentiment (Press Enter once done)"))
        if len(data) > 0:
            data = analyze_sentiment(data)
            st.subheader("The result for Entered Data :{}".format(data))



    elif choice == "Login":
        st.subheader("Please Enter Valid Credentials")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login/Logout"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:
                st.success("Logged In as {}".format(username))

                st.sidebar.success("login Success.")
                uploaded_file = st.file_uploader("Choose a file")
                if uploaded_file is not None:
                    df = pd.read_csv(uploaded_file)
                    df['clean_tweet'] = df['Review'].apply(lambda x: clean_tweet(x))
                    df["Sentiment"] = df["Review"].apply(lambda x: analyze_sentiment(x))
                    st.write(
                        "Total Positive Reviews are : {} | Total Negative Reviews are : {} | Total Neutral Reviews are : #{}".format(
                            len(df[df["Sentiment"] == "Positive"]), len(df[df["Sentiment"] == "Negative"]),
                            len(df[df["Sentiment"] == "Neutral"])))
                    st.write(df)
                    st.subheader(" Count Plot for Different Sentiments")
                    st.write(sns.countplot(df["Sentiment"]))
                    st.pyplot()
                    if (len(df[df["Sentiment"] == "Positive"]) > len(df[df["Sentiment"] == "Negative"])):
                        st.subheader(" This application is not fraudelent.")
                    else:
                        st.subheader(" This application has the potential to be fraudulent.")
            else:
                st.warning("Incorrect Username/Password")




    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")


if __name__ == '__main__':
    main()
