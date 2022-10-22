

# import wordlist
# ask for and set center letter
# ask for and set other letters
# set minimum word length
# identify legal wordlist
# identify pangram
# print results

# alternative import wordlist
# import requests
#
# r = requests.get('[url]')
# words = r.text
# lines = words.splitlines()

# import wordlist
# using TWL06, the official Scrabble Wordlist from https://www.wordgamedictionary.com
import random
import string
#
word_file = open('twl06.txt', 'r')
word_list = []
for l in word_file.readlines():
    word_list.append(l.strip())
word_file.close()



ctrltr = input("What's the center letter of the beehive?")
if len(ctrltr) != 1:
    feedback = "I only accept a single letter. Please enter the center letter again."
    print(feedback)

outerltrs = input("What are the outer letters of the beehive?")
# letter order irrelevant
if len(set(outerltrs)) != 6:
    feedback = "Please provide six unique letters."
    print(feedback)

min_length = int(input("What is the minimum word length?"))
if min_length > 10:
    feedback = "Please provide single digit number."
    print(feedback)

beehive = ctrltr + outerltrs
#
# randomltr = random.choice(beehive)
#
# # def generate_Word(beehive):
# #     # word = ""
# #     # for i in random.randint(min_length, max_length):
# #     word = ''.join(random.choice(beehive) for i in range(8))
# #     #     word += random.choice(beehive)
# #     # word = ''.join(random.choice(beehive) for i in range(min_length, max_length))
# #     # word = ''.join(random.choice(beehive) for i in random.randint(min_length, max_length))
# #     print(word)
# #     return word
# #
# #     for count in xrange(0,wmaximum):
# #       for x in random.sample(alphabet,random.randint(minimum,maximum)):
# #           string+=x
# much much faster to select random word and check against beehive, then generate random string from beehive ltters and check against wordlist
##

# def check_word(word):
#     if (ctrltr in word) and (len(word) > 3):
#         if word in word_list:
#             good_words.append(word)
#             return word
#     #     else:
#             print('not a valid word')
#     else:
#         print('no center letter')

# how to stop looking for words
    # max out at 200 good words but not unique
    #     if uinque, don't know when to stop loop --   use time out?
    # only works for known beehives

valid_words = []
pangrams = []
def main():
    count = 0
    while (len(valid_words) < 300):
        # word = generate_Word(beehive)
        word = random.choice(word_list)
        count += 1
        if (ctrltr in word) and (set(word).issubset(set(beehive))) and (len(word) > (min_length-1)):
            valid_words.append(word)
        if set(word) == set(beehive):
            pangrams.append(word)
    print(count)
main()
results = set(valid_words)  # reduce to unique valid words
print(sorted(results, key=lambda item: (-len(item), item))) # sort by longest to shortest, then alpahbetically
print(set(pangrams))
