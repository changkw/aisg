import requests
from collections import Counter

def fetch_and_analyze_text(url):
    # Fetch the text file
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the text file.")
        return
    
    text = response.text.lower()

    # Remove non-alphanumeric characters (excluding spaces)
    cleaned_text = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text)
    words = cleaned_text.split()

    # Count word frequencies
    word_counts = Counter(words)
    most_common = word_counts.most_common()

    # Extract the 10th to 20th most frequent words
    top_words = most_common[9:20]  # 10th to 20th index
    print("Words ranked from 10th to 20th by frequency:")
    for word, freq in top_words:
        print(f"{word}: {freq}")


fetch_and_analyze_text("https://www.gutenberg.org/cache/epub/16317/pg16317.txt")
