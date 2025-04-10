import pandas as pd
from hazm import Normalizer, word_tokenize
import re

# Word List Name
Worldlist_Name = "big"

def clean_unicode(text):
    """
    Remove invalid Unicode characters and non-Persian symbols
    """
    if not isinstance(text, str):
        text = str(text)
    
    # Remove Unicode control characters (e.g., [u204])
    text = re.sub(r'\[u[0-9A-Fa-f]+\]', '', text)
    
    # Remove non-Persian characters (only Persian letters, numbers, and spaces allowed)
    text = re.sub(
        r'[^\u0600-\u06FF\uFB8A\u067E\u0686\u06AF\u200C\u200F0-9\s]', 
        '', 
        text
    )
    
    return text.strip()

try:
    # Read the vocabulary file
    wordlist = pd.read_csv(f"Vocab/Raw/{Worldlist_Name}.txt", header=None, names=["words"], on_bad_lines='skip')
    
    # Preprocessing: Remove invalid Unicode characters
    wordlist["cleaned"] = wordlist["words"].apply(clean_unicode)
    
    # Normalization with Hazm (keeping diacritics)
    normalizer = Normalizer(remove_diacritics=False)
    wordlist["normalized"] = wordlist["cleaned"].apply(
        lambda x: normalizer.normalize(str(x))
    )
    
    # Tokenize: Split attached words into separate tokens
    wordlist["tokenized"] = wordlist["normalized"].apply(
        lambda x: word_tokenize(x)
    )
    
    # Flatten the list of tokens into a single list
    all_tokens = [token for sublist in wordlist["tokenized"] for token in sublist]
    
    # Convert to Series for further processing
    tokenized_series = pd.Series(all_tokens)
    
    # Count word frequencies
    word_counts = tokenized_series.value_counts()
    duplicates = word_counts[word_counts > 1]
    
    # Extract unique words
    unique_words = tokenized_series.drop_duplicates().tolist()
    
    # Print results
    print("Number of duplicate words:", len(duplicates))
    print("Sample of duplicate words:")
    print(duplicates.head(10))
    print("Unique words sample:", unique_words[:10])
    
    # Save the result (each token in a separate line)
    pd.Series(unique_words).to_csv(f"Vocab/Normilized_{Worldlist_Name}.txt", index=False, header=False)
    
except pd.errors.ParserError as e:
    print(f"Error reading file: {e}")
except Exception as e:
    print(f"Unknown error: {e}")