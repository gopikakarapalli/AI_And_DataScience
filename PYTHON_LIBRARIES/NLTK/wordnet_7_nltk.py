import nltk

print(nltk.__file__)

#wordnet
from nltk.corpus import wordnet

#"program" to find synsets like so:
syns = wordnet.synsets("program")
#Just the word:
print(syns[0].name())

print(syns[0].lemmas()[0].name())
#Definition of that first synset:

print(syns[0].definition())
#Examples of the word in use:
print(syns[0].examples())

'''
Next, how might we discern synonyms and antonyms to a word? The lemmas will be
synonyms, and then you can use .antonyms to find the antonyms to the lemmas.
As such, we can populate some lists like:

'''
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print('synonyms:-\n',set(synonyms))
print('antonyms:-\n',set(antonyms))
