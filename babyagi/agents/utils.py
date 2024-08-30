def clean_text(text):
    return text.strip().replace("\n", " ")


def format_sentiment(scores):
    return f"(compound {scores['compound']}) (positive {scores['pos']}) (neutral {scores['neu']}) (negative {scores['neg']})"
