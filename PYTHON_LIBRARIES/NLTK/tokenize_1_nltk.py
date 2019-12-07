import nltk
#nltk.download()
#d (for download)
#all (for download everything)


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

'''
Corpus - Body of text, singular. Corpora is the plural of this. Example: A collection of medical journals.
Lexicon - Words and their meanings. Example: English dictionary. Consider, however, that various fields will have different lexicons. For example: To a financial investor, the first meaning for the word "Bull" is someone who is confident about the market, as compared to the common English lexicon, where the first meaning for the word "Bull" is an animal. As such, there is a special lexicon for financial investors, doctors, children, mechanics, and so on.
Token - Each "entity" that is a part of whatever was split up based on rules. For examples, each word is a token when a sentence is "tokenized" into words. Each sentence can also be a token, if you tokenized the sentences out of a paragraph.
'''
EXAMPLE_TEXT = """Hello Mr. Smith, how are you doing today? The weather is great,
and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."""

print('sent_tokenize:\n',sent_tokenize(EXAMPLE_TEXT))
print('word_tokenize:\n',word_tokenize(EXAMPLE_TEXT))


#               ---------- stop words ---------------
example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]
'''
filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)'''

print(word_tokens)
print(filtered_sentence)



