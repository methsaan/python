#! /usr/bin/python3

from collections import Counter

text = "but why waa who woo woo waa woo which"

words = text.split()

counter = Counter(words)
topThree = counter.most_common(3)
print(topThree)
