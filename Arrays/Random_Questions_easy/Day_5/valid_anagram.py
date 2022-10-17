"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

"""

s = input()
t = input()
def count_alphabets(word):
    word_dict = {}
    for alphabet in word:
        if alphabet not in word_dict.keys():
            word_dict[alphabet] = 1
        else:
            word_dict[alphabet] +=1
    return word_dict

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    s_dict = count_alphabets(s)
    t_dict = count_alphabets(t)
    if s_dict == t_dict:
        return True
    return False

print(isAnagram(s,t))

