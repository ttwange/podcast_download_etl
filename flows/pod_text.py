from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Perform sentiment analysis
    sentiment = blob.sentiment
    
    return sentiment

if __name__ == "__main__":
    file_path = "./econ.txt"
    
    # Read the text from the file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    # Perform sentiment analysis on the text
    sentiment = analyze_sentiment(text)
    
    # Print the sentiment analysis results
    print("Sentiment Polarity:", sentiment.polarity)
    print("Sentiment Subjectivity:", sentiment.subjectivity)
    
    # Interpret the sentiment
    if sentiment.polarity > 0:
        sentiment_label = "Positive"
    elif sentiment.polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    print("Sentiment:", sentiment_label)
