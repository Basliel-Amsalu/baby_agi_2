import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from hyperon import *
from .utils import clean_text, format_sentiment


sid = SentimentIntensityAnalyzer()

def advanced_analyze_sentiment(metta: MeTTa, *args):
    text = clean_text(str(args[0]))
    scores = sid.polarity_scores(text)
    formatted_scores = format_sentiment(scores)
    print(f"Sentiment: {formatted_scores}")
    sentiment_atom = metta.parse_all(formatted_scores)
    return [ValueAtom(sentiment_atom, 'Expression')]
