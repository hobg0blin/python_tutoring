import nltk
import random
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
import re
prondict = nltk.corpus.cmudict.dict()

#the goal of this program is to make a list of all words that match that last two phonemes and the three prior words
# this is much better than the old version but here's a refactored version with a few changes:
# next step would be to see what you can take out and put into its own function - there are 2 or 3 discrete steps here
# that might make this function cleaner if they were separated out
def refactored_find_phonemes(num, ph_list, sentences):
    #if outputlist is, presumably, an empty list, there's no reason to include it in the declaration
    output = []
    #same thing with range - if we're just using array[i], it's simpler to just use for in on the array itself
    for i in sentences:
        sent = i.split()
        for j in range(len(sent)):
            word = re.sub(r'[^\w\s]', '', sent[j].lower())
            #why are we checking "isalpha?"
            if word in prondict:
                syl = prondict[word]
                print('syl: ', syl)
                pho = syl[-1][num:]
                # if pho == ph_list then it's definitely longer than 1, so we don't need to check that
                #same with j-num, presumably - j is always going to be part of the existing array
                if pho == ph_list and len(word)>3:
                    location = j
                    phrase = sent[location-3:location+1]
                    print('pho: ', pho)
                    output.append(phrase)
    return output






def find_phonemes(num, ph_list, sentences, outputlist):
    print('sentences: ', sentences)
    for i in range(len(sentences)): #could these first two lines be written like list comprehensions
        this_s = sentences[i].split()
        for j in range(len(this_s)):
            word = re.sub(r'[^\w\s]', '', this_s[j].lower())
            if word in prondict and word.isalpha():
                syllable = prondict[word]
                #print('sylabble: ', syllable)
                pho = syllable[-1][num:]
                if len(pho) > 1 and pho == ph_list and j-num>0 and len(word)>3:
                    location = j
                    phrase = this_s[location - 3], this_s[location - 2], this_s[location - 1], word
                    outputlist.append(phrase)
    return outputlist

def gen_rhyme_pair(rhyme_list):
    r1 = random.randint(0, len(rhyme_list)-1)
    r2 = random.randint(0, len(rhyme_list)-1)
    if r1 == r2:
        r2 = random.randint(0, len(rhyme_list)-1)
    n1 = ' '.join(rhyme_list[r1])
    n2 = ' '.join(rhyme_list[r2])
    return (n1 + '\n' + n2)

def gen_one_phone(rhyme_list):
    r1 = random.randint(0, len(rhyme_list)-1)
    n1 = ' '.join(rhyme_list[r1])
    return (n1)

phoneBeg = 1
phoneBeg2 = 2
matchPh = ['DH', 'AH0']
# allit_list = []
def find_alliteration(sentence, outputlist):
    #this function returns a list of two word strings
    for i in range(len(sentence)):
        this_s = sentence[i].split()
        for j in range(len(this_s)-1):
            word = re.sub(r'[^\w\s]', '', this_s[j].lower())
            word2 = re.sub(r'[^\w\s]', '', this_s[j+1].lower())
            # print(word, word2)
            if word in prondict and word.isalpha() and word2 in prondict and word2.isalpha():
                syllable = prondict[word]
                syllable2 = prondict[word2]
                # print(syllable)
                # print(syllable2)
                pho = syllable[-1][:phoneBeg2]
                next_pho = syllable2[-1][:phoneBeg2]
                # print(pho, next_pho)

                # print(word, syllable, ' the pho is ', pho, word2, syllable2, 'the next pho is ', next_pho)
                # finds alliteration for words greater than three letters long
                if pho == next_pho and len(word)>3 and len(word2)>3:
                    location = j
                    # a_phrase = word, word2
                    a_phrase = word +" " + word2
                    # print(word, word2)
                    outputlist.append(a_phrase)
    return outputlist


def convert_lowercase(text):
    return [word.lower() for word in text]

# remove punctuation from the string
def remove_punctuation(text):
    exclude = set(string.punctuation)
    keep_these_punct = ['/', '%', '-']
    for punct in keep_these_punct:
        exclude.remove(punct)
    converted_text = ''.join(ch for ch in text if ch not in exclude)
    return converted_text

#choose a pair and convert it from a tuple to string
# my_tuple = gen_rhyme_pair()
# my1 = ' '.join(my_tuple[0])
# my2 = ' '.join(my_tuple[1])
# print(my1)
# print(my2)

def gen_rando():
    return random.random()