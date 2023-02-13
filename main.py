import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
unpunc_text = lower_case.translate(str.maketrans('', '', string.punctuation))
token_words = unpunc_text.split()
# print(token_words)
# stop words are the ones which do not add meaning to the sentence
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
finWord = []
for word in token_words: 
    if word not in stop_words:
        finWord.append(word)
# print(finWord)
emotionList=[]        
with open('emotions.txt', 'r') as newFile:
    for i in newFile:
        clearNewlines = i.replace('\n', '').replace(
            ',', '').replace("'", '').strip()
        word, emotion = clearNewlines.split(':')
        # print(clearNewlines)
        
        if word in finWord:
            emotionList.append(emotion)
# print(emotionList)  
count = Counter(emotionList)
print(count)
fig, ax =plt.subplots()
ax.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig('emotionsGraph.png')
plt.show()
