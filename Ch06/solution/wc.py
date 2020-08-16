"""Print count of words (ignoring case)"""
from collections import Counter
import unicodedata


def normalize(word):
    """Normalize word"""
    word = unicodedata.normalize('NFKC', word)
    return word.casefold()


wc = Counter()
with open('words.txt', encoding='utf-8') as fp:
    for word in fp:
        word = word.strip()
        wc[normalize(word)] += 1

for word, count in wc.most_common():
    print(f'{word:<15}\t{count}')
