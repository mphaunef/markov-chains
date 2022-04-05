"""Generate Markov text from text files."""

import sys
from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents


def make_chains(text_string, n):

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    words = text_string.split()

    for i in range(len(words) - n):


        word_key = tuple(words[i:i+n])

        #print(word_key)

        chains[word_key] = chains.get(word_key, []) + ([words[i+n]]) 

    #print(chains)

    return chains


def make_text(chains):
    """Return text from chains."""
    
    words = []

    word_keys = list(chains.keys())

    cur_key = choice(word_keys)
    words += list(cur_key)

    # your code goes here
    while cur_key in chains:

        chosen_word = choice(chains[cur_key])
        #print(cur_key)
        #print(chosen_word)
        words.append(chosen_word)
        new_key_list = list(cur_key[1::])
        new_key_list.append(chosen_word)
        new_key = tuple(new_key_list)
        #print(new_key)

        cur_key = new_key
    #print(words)


    return ' '.join(words)


input_path = 'green-eggs.txt'
n = 6

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains)

print(random_text)

