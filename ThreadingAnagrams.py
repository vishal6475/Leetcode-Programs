from threading import Thread
import time

value = True

class AreAnagramsThread(Thread):
    def __init__(self, hs1, s2):
        Thread.__init__(self)
        self.hs1 = hs1
        self.s2 = s2

    def run(self):
        global value
        hs2 = dict()

        for c in self.s2:
            if c not in ('!', '.', ',', '?', ' '):
                c = c.lower()
                hs2[c] = 1 + hs2.get(c, 0)

        if self.hs1 != hs2:
            value = False

    

def are_anagrams(s1, *df):
    global value
    
    value = True

    
    hs1 = dict()

    for c in s1:
        if c not in ('!', '.', ',', '?', ' '):
            c = c.lower()
            hs1[c] = 1 + hs1.get(c, 0)

    for s2 in df:
        th = AreAnagramsThread(hs1, s2)
        th.start()
        
    
    #print(hs1)
    #print(hs2)    

    time.sleep(1)

    return value


result = are_anagrams("auctioned", "cautioned", "educatdion")
print(result)  
#"""
assert are_anagrams("elvis", "lives") == True
assert are_anagrams("cinema", "iceman") == True
assert are_anagrams("below", "elbow") == True
assert are_anagrams("desert", "stressed") == False
assert are_anagrams("desserts", "stressed") == True
assert are_anagrams("night", "thin") == False
assert are_anagrams("night", "thing") == True 

assert are_anagrams("Elvis Aaron Presley", "Seen alive? Sorry, pal!") == True
assert are_anagrams("easy as 123", "A Essay 312") == True
assert are_anagrams("eleven plus two", "12 plus 1") == False
assert are_anagrams("l33tc0de", "33 dole") == False
assert are_anagrams("O, Draconian devil!", "Leonardo da Vinci") == True
assert are_anagrams("why I net shark peoples", "whey protein shake, pls") == True

assert are_anagrams("auctioned", "cautioned", "education") == True
assert are_anagrams("auctioned", "cautioned") == True
assert are_anagrams("auctioned") == True
assert are_anagrams("bad credit", "debit card", "rad cd, I bet", "brad cited") == True
assert are_anagrams("bad credit", "debit card", "rad cd, I bet", "red tea bid") == False
#"""

# Extend your solution to take any number of words. This solution should work with spaces, punctuation, and numerical characters similar to part 2.

# # Part 3 test cases
# assert are_anagrams("auctioned", "cautioned", "education") == True
# assert are_anagrams("auctioned", "cautioned") == True
# assert are_anagrams("auctioned") == True
# assert are_anagrams("bad credit", "debit card", "rad cd, I bet", "brad cited") == True
# assert are_anagrams("bad credit", "debit card", "rad cd, I bet", "red tea bid") == False

#"""
# Extend your solution to support spaces, punctuation, upper cases, and numerical characters.

# Punctuation will be limited to ‘!’, ‘.’, ‘,’, ‘?’
# Punctuation and spaces are not part of the anagram
# Numbers are included in the anagram
# Case insensitive
# # Part 2 test cases
# assert are_anagrams("Elvis Aaron Presley", "Seen alive? Sorry, pal!") == True
# assert are_anagrams("easy as 123", "A Essay 312") == True
# assert are_anagrams("eleven plus two", "12 plus 1") == False
# assert are_anagrams("l33tc0de", "33 dole") == False
# assert are_anagrams("O, Draconian devil!", "Leonardo da Vinci") == True
# assert are_anagrams("why I net shark peoples", "whey protein shake, pls") == True

# Your previous Markdown content is preserved below:

# An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Given two strings, write a function to check if they're are anagrams of each other.

# For example:

# ```
# s1 = "elvis"
# s2 = "lives"
# result = are_anagrams(s1, s2)
# print(result) # True
# ```

# A few invariants hold true:

# - The strings will only contain lower case alphabetical characters
# - There will be no spaces
# - The input will always be valid

# ```
# # Part 1 test cases
# assert are_anagrams("elvis", "lives") == True
# assert are_anagrams("cinema", "iceman") == True
# assert are_anagrams("below", "elbow") == True
# assert are_anagrams("desert", "stressed") == False
# assert are_anagrams("desserts", "stressed") == True
# assert are_anagrams("night", "thin") == False
# assert are_anagrams("night", "thing") == True
# ```