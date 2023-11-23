import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class Sentiment_analyser:

    def __init__(self):
        self.sentiment = None
        nltk.download('vader_lexicon')
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')

    @staticmethod
    def preprocessing(text):
        tokens = word_tokenize(text.lower())
        without_stop_words = [token for token in tokens if token not in stopwords.words('english')]
        lemmatized = [WordNetLemmatizer().lemmatize(token) for token in without_stop_words]
        finished_text = " ".join(lemmatized)
        return finished_text

    @staticmethod
    def determine_sentiment(text):
        analyser = SentimentIntensityAnalyzer()
        scores = analyser.polarity_scores(text)
        if scores['pos'] > 0:
            sentiment = 1
        else:
            sentiment = 0
        return sentiment

    def process(self, text):
        text = self.preprocessing(text)
        self.sentiment = self.determine_sentiment(text)

    def get_sentiment(self):
        return self.sentiment


