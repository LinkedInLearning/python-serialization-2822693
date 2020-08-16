"""Print count of words (ignoring case)"""
from collections import Counter


wc = Counter()
with open('words.txt', encoding='utf-8') as fp:
    for word in fp:
        word = word.strip()
        wc[word] += 1

for word, count in wc.most_common():
    print(f'{word:<15}\t{count}')
