# Detection Of Fraud Apps Using Sentimental Analysis.

# Introduction :
Most of us now use Android and IOS mobile devices, and we frequently use the  play store or app store functionality. 
Both stores offer a large number of applications, but unfortunately, a small number of those applications are fraudulent.
Such applications can cause damage to the phone and may also be data thieves. As a result, such applications must be labelled
so that store patrons can identify them.
     we propose a web application that will process the information, comments, and application review. As a result, it will be easier 
to determine whether an application is fraudulent or not. With the web application, multiple applications can be processed at the same time.
Furthermore, users may not always find accurate or true product reviews on the internet. As a result, the admin will evaluate the ratings and comments, 
and it will be simple for the admin to determine whether the application is genuine or fraudulent.


#Architecture:

1. Data Collection
   └── Sources: App store reviews (Google Play, App Store)
       └── Tools: APIs, Web scraping (BeautifulSoup, Scrapy)

2. Preprocessing
   └── Clean and preprocess text:
       ├── Tokenization
       ├── Stopword removal
       └── Lemmatization
   └── Tools: NLTK, TextBlob

3. Sentiment Analysis
   └── Use sentiment classifiers:
       ├── TextBlob (rule-based)
       └── Machine learning models (e.g., Naive Bayes, BERT)
   └── Outputs:
       ├── Positive Reviews
       ├── Neutral Reviews
       └── Negative Reviews

4. Feature Extraction
   ├── Extract textual features:
   │   ├── Keywords (e.g., "scam", "fraud", "stolen")
   │   └── Sentiment polarity
   ├── Metadata features:
   │   ├── App ratings
   │   └── Update logs
   └── User behavioral features:
       └── Trends like download spikes or negative review surges

5. Fraud Classification
   ├── Inputs:
   │   ├── Sentiment scores
   │   ├── Metadata
   │   └── Behavioral patterns
   ├── Algorithms:
   │   ├── Machine learning (Random Forest)
   │   └── Deep learning (RNN)
   └── Outputs:
       ├── Fraudulent Apps
       └── Genuine Apps

6. Visualization & Reporting
   ├── Dashboards:
   │   ├── Sentiment breakdown
   │   ├── Fraud detection results
   │   └── App statistics
   └── Tools:
        └── Matplotlib/Seaborn

7. Feedback Loop
   └── Model retraining with updated reviews and evolving fraud patterns.

#Software Technologies used:

Programming Language – Python
Libraries – Pandas, NumPy, SQLite, Textblob, Matplotlib, Seaborn
Database – SQLite3 
Framework – Streamlit (user Interface using python)
Tools – Visual Studio Code

# Project Advantages:

The proposed framework is scalable and can be expanded to detect ranking fraud using other domain-generated evidence.
The system will reduce fraudulent activities.
Reduce the loss due to fraudulent activities. 


# Project Steps / Algorithm:

1.Start
2.Enter Review / Upload CSV file
3.Read App reviews from CSV file
4.Perform Tokenization
5.Remove stop words from reviews
6.Lemmatization
7.Calculate Sentiment for each review using Text Blob Library  
8.Categorize review – Positive, Negative, and Neutral
9.Visualize the Result  

# Conclusion:
   The main objective of the proposed work was to review fraud detection of apps and to use a sentiment analysis 
approach to differentiate the particular fraud apps. The experimental analysis is carried out on differing types of 
apps with the proposed method for the detection of fraud apps. 
Our system can detect frauds using Natural Language Processing and machine learning techniques. 
Further, an optimization-based aggregation method combines all three pieces of evidence to detect fraud.
Different class values and threshold values give different accuracy results of the time required for execution.
