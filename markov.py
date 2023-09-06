"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)

    words = file.read()

    return words



def make_chains(text_string):
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

    text_words = text_string.split()
    n = 0

    for word in text_words:
        while (n + 2) < len(text_words):            

            current_key = (text_words[n], text_words[n+1])
            follow_word = (text_words[n+2])
    
            if current_key in chains == False:
                chains[current_key] = follow_word
                n += 1
            
            else:
                chains[current_key] #need to add value to a list , chains[current_key] = []???   Can we append??  extend??
                n += 1

    
    
    print(chains)


    
    

    # print(text_words)

    #for word in text_words:
    #    text_words[::2]

    #return chains

print(make_chains("hi there mary hi there juanita"))
def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
