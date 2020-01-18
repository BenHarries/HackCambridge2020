from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import random


def sentence_finder(word):
    text = open("storybooks.txt").read()
    sentences = sent_tokenize(text)
    # this gave you the all sentences that your special word is in it !
    senten = [sent for sent in sentences if word in word_tokenize(sent)]
    if len(senten) != 0:
        return random.choice(senten)
    else:
        return random.choice(sentences)


incorrectWord = "banana"
print(sentence_finder(incorrectWord))
