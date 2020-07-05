# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.
from collections import Counter, defaultdict

paragraph = """This paragraph is going to contain anagrams.  There is an arc
            through which you can drive a car quickly.  That ant has a tan face.
            I have tons of snot fo you. And then ouch said the chou man.  I hit
            the ram in his arm pit"""

sorted_words = list(set(paragraph.split()))

finding_anagrams = defaultdict(list)
anagrams = []
for word in sorted_words:
    finding_anagrams[''.join(sorted(word))].append(word)


for anagram in word_separated:
    if len(finding_anagrams[anagram]) > 1:
        anagrams.append(word_separated[anagram])

print(anagrams)
