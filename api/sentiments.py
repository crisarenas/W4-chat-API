import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
nltk.download("vader_lexicon")
nltk.download("stopwords")


#SIA - Sentiments Intensity Analyzer
sia = SentimentIntensityAnalyzer()