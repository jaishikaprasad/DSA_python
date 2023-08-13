# Leetcode Ques : 242 [Valid Anagram]

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def valid_anagram(s,t):
    count_s = {}
    count_t = {}
    if len(s) != len(t):
        return False
    for i in s:
        if i in count_s:
            count_s[i] += 1
        else:
            count_s[i] = 1

    for i in t:
        if i in count_t:
            count_t[i] += 1
        else:
            count_t[i] = 1

    if count_s == count_t:
        return True
    else:
        return False
    
s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))

# Output : True