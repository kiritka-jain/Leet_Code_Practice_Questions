"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

s = input()
words = s.split(" ")
print(words)
words_len = len(words)
for word in range(words_len-1,-1,-1):
    if words[word] != "":
        print(len(words[word]))
