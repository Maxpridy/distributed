
from textblob import TextBlob
from collections import Counter

nounlist=[]

with open('output_htmlrfc.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
    f.close()


with open('output_htmlrfc_noun.txt','w',encoding='utf-8') as f:
    for line in lines:
        blob = TextBlob(line)
        for noun in blob.noun_phrases:
            f.write(noun + " ")

    f.close()


#counts = Counter(nounlist)
#print(counts.most_common(10))
