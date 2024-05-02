from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def is_spam(text, custom_filter_words=[]):
  """
  This function classifies text as spam or not spam.

  Args:
      text: The Telugu text to be classified.
      custom_filter_words: A list of additional Telugu words to consider as spam indicators.

  Returns:
      True if the text is classified as spam, False otherwise.
  """
  # Load Telugu stopwords
  telugu_stopwords = stopwords.words('telugu')

  # Combine custom filter words with stopwords
  all_filter_words = telugu_stopwords + custom_filter_words

  # Tokenize the text (split into words)
  tokens = word_tokenize(text)

  # Filter out stopwords and lowercase all words
  filtered_tokens = [word.lower() for word in tokens if word not in all_filter_words]

  # Implement your spam detection logic here
  # This example checks for a certain percentage of filter words
  spam_ratio = sum(word in filtered_tokens for word in custom_filter_words) / len(filtered_tokens)
  threshold = 0.2  # Adjust this threshold as needed (e.g., 0.3 for stricter)

  return spam_ratio > threshold

# Example usage
text1 = "ఈ రోజు ఉచిత బహుమతి గెలుచుకోండి! ఇప్పుడే క్లిక్ చేయండి!"  # Spam message
text2 = "ఎలా ఉన్నారు? కొత్త సినిమా చూశారా?"  # Not spam

custom_filter_words = ["ఉచితం", "బహుమతి"]  # Add your custom Telugu spam words

print(f"Text 1 (Spam): {is_spam(text1, custom_filter_words)}")
print(f"Text 2 (Not Spam): {is_spam(text2, custom_filter_words)}")
