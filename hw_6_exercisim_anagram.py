"""
Introduction
An anagram is a rearrangement of letters to form a new word. Given a word and a
list of candidates, select the sublist of anagrams of the given word.

Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana"
the program should return a list containing "inlets".

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should
include a meaningful error message to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do,
the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the
exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")
"""


def anagram(word, ls):
    def create_hist(word):
        hist = dict()
        for char in word:
            hist[char] = hist.get(char, 0) + 1
        return hist
    comp_hist = create_hist(word)
    return [word for word in ls if create_hist(word) == comp_hist]


print(anagram("listen", ["enlists", "google", "inlets", "banana"]))
