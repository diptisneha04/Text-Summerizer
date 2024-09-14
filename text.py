import nltk
import heapq

from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

fl = open("D:/The Forgotten Lighthouse.txt","r",encoding="UTF-8")
text = fl.read()
text1 = text.lower()

eng_stopwords = set(stopwords.words('english'))

sentence_list = nltk.sent_tokenize(text1)

# Making a dictionary of frequency scores to words {word: frequency}
freq = {}
word_list = nltk.word_tokenize(text1)

for word in word_list:
    if word not in eng_stopwords:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

max_frequency = max(freq.values())

for word in freq:
    freq[word] = freq[word] / max_frequency

sent_scores = {}

# Setting sentence scores based on word scores
for sent in sentence_list:
    for word in nltk.word_tokenize(sent):
        if word in freq and len(sent.split(' ')) < 35:
            if sent not in sent_scores:
                sent_scores[sent] = freq[word]
            else:
                sent_scores[sent] += freq[word]

# Finding top 10 sentences based on scores
summary = heapq.nlargest(10, sent_scores, key=sent_scores.get)

for a in summary:
    print(a)