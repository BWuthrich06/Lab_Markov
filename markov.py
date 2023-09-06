"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)

    words = file.read()
    file.close()

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
        if (n + 2) < len(text_words):            
           
            current_key = (text_words[n], text_words[n+1])
            follow_word = text_words[n+2]
            

            if current_key in chains:
                chains[current_key].append(follow_word)   
                n += 1

            else: 
                chains[current_key] = []
                chains[current_key].append(follow_word)
                n += 1

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    key_list = list(chains.keys())              #change into list
   
    random_key = choice(key_list)               #getting a random key
    
    for word in random_key:
        words.append(word)                      #adding each word from key into words  (have 2 words)

    # print("initial key added >> ", words)

    random_value = chains[random_key]           #Assigning the random key value list
    transition_value = choice(random_value)     #Random value chosen and assigned to transition value
    words.append(transition_value)              #Adding value to words list

    # print("after first append >> ", words)

    

    while True:
        new_key = tuple(words[-2:])                        
        # print("new key made ", new_key)
        
        if new_key in chains:
            random_value = chains[new_key]

            # print("random value found >> ", random_value)

            transition_value = choice(random_value)

            # print("transition value >> ", transition_value)
            words.append(transition_value)
        else:
            break

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
