# NYT Spelling Bee Cheat

The _New York Times_ added a daily puzzle called ["Spelling Bee"](https://www.nytimes.com/puzzles/spelling-bee). The puzzle gives you seven letters in a hive (one in the center of the hive, surrounded by six other letters). You must make as many words as you can from those seven letters, as long as you comply with these rules:
 1. you must include the center letter;
 2. you can repeat letters as often as you want;
 3. the words must be at least four letters long (five letters long in Sunday's _A Little Variety_ puzzle pack). No 'cat' or 'if'.

You get one point for each valid word and three points for a word that uses all seven letters (a pangram). Each puzzle contains at least one pangram.

Unlike the NYT crosswords, you can't check your answers right away; you have to wait until the following day. Furthermore, you can only check yesterday's answers, so if you want to go back to last week's answers, you can't. So I needed a way to check my answers. I especially needed a way to find the pangram, because no matter how many words I found, if I had not found the pangram, my day was ruined.

So I wrote a little Python script. I hope it helps.

# Comments

My basic outline was the following:
 1. import wordlist
 2. ask for and set center letter
 3. ask for and set other letters
 4. ask for and set minimum word length
 5. identify legal wordlist
 6. identify pangram
 7. print results

## Import Wordlist (Step 1)

I'm using the Official Scrabble Tournament Word List (twl06) that I grabbed from https://www.wordgamedictionary.com and just downloaded to a .txt file and stripped the headers. If and when I make this into a web app, I'll have to figure out how to call a dictionary API. The NYT seems to use a smaller dictionary, as valid TWL06 words are not accepted by the NYT. 

## Setting Puzzle (Steps 2-4)

I could do better on input validation, but for now I've assumed the user (me) knows the drill.

## Identifying Legal Words (Step 5)

This turned into a lesson in computational time. Initially, I thought I would generate random strings from the letter set and then test the string against the dictionary. One issue was the word length. I thought setting a maximum of 20 letters would be enough to find at least one pangram, but going through 26^20 letter combinations (and then 26^19, 26^18, etc.) was taking too long and I realized there had to be better way. Fortunately, that didn't take long to figure out, so I went to plan B.

I would randomly select a word from the dictionary and see if it matched my letter set and rules. This was much faster. Now my problem was to figure out how many iterations to ask for or when to step out of a while loop. I decided to randomly select words until I reached 300 valid words. There would be repeats, but that seemed high enough to ensure I got the pangram. That's been true so far, except once, and even then I got the pangram on the next run.  

## Identifying Pangram (Step 6)

This was just a matter of identifying whether a given words contains all the letters of the beehive: `if set(word) == set(beehive)` 

## Printing Results (Step 7)

I used the `set` datatype to reduce my results list to unique words. Then I ordered from longest to shortest (longer words get more points) and then alphabetically.  

I also print out the count of random words selected out of curiosity. I've seen counts range from 500,000 to 900,000 so far.

