import nltk
import heapq

from nltk.corpus import stopwords
from  nltk.tokenize import sent_tokenize
from  nltk.tokenize import word_tokenize


fl=open("D:\SNEHA mca project\Text summerizer\The Forgotten Lighthouse.txt","r",encoding="UTF-8")
text=fl.read()
text1=text.lower()

eng_stopwords = set(stopwords.words('english'))
sentence_list = sent_tokenize(text1)

freq = {} 
word_list = word_tokenize(text1) 

for i in word_list:
    if i not in eng_stopwords:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

max_frequency = max(freq.values()) 

for word in freq:
    freq[word] = freq[word] / max_frequency 

sent_scores = {}

for sent in sentence_list:
    for word in word_list:
        if word in freq and len(sent.split(' ')) < 50:
            if sent not in sent_scores:
                sent_scores[sent] = freq[word]
            else:
                sent_scores[sent] += freq[word]

summary = heapq.nlargest( 10,sent_scores, key=sent_scores.get)

for a in summary:           
       print(a) 

