def simple_summarizer(text, num_sentences=3):
    # Split the text into sentences
    sentences = text.split('.')
    
    # Count the occurrence of each word in the text
    word_freq = {}
    for word in text.split():
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    
    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.split():
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
    
    # Get the summary
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return '. '.join(summary_sentences)

# Example usage
fl = open("D:/The Forgotten Lighthouse.txt","r",encoding="UTF-8")
text_corpus=fl.read()
summary = simple_summarizer(text_corpus)
print("Summary:", summary)
