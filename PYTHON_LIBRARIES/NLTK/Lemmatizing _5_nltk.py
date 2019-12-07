#lemmatizer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))# cat
print(lemmatizer.lemmatize("cacti"))#cactus
print(lemmatizer.lemmatize("geese"))#goose
print(lemmatizer.lemmatize("rocks"))#rock
print(lemmatizer.lemmatize("python"))#python
print(lemmatizer.lemmatize("better", pos="a"))#good
print(lemmatizer.lemmatize("best", pos="a"))#best
print(lemmatizer.lemmatize("run"))#run
print(lemmatizer.lemmatize("run",'v'))#run








