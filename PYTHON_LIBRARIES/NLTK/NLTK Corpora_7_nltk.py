import nltk

print(nltk.__file__)# NLTK Corpora location

#wordnet
from nltk.corpus import wordnet

#"program" to find synsets like so:
syns = wordnet.synsets("program")
#Just the word:
print('name:',syns[0].name())

print('lemmas.name:',syns[0].lemmas()[0].name())
#Definition of that first synset:

print('definition:',syns[0].definition())
#Examples of the word in use:
print('examples:',syns[0].examples())
print('--------------------------------------------------------------')
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


# Let's compare the noun of "ship" and "boat:"

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))
#0.9090909090909091

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))
#0.6956521739130435

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
#0.32

