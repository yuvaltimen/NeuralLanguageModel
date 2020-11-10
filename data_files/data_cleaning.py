import re
from nltk import sent_tokenize

"""
Some problems we want to deal with in our cleaning process:
1. Punctuation and hyphens (many instances of '--')
2. British spellings (colour, behaviour, phaenomenon)
3. Different cases

"""

favour, endeavour, colour, behaviour, \
possest


def clean_data(file_path):
    """Given a file path, this function creates a new file with
    the cleaned data, one sentence per line.
    Parameters:
        file_path (str) - The path of the data
    Returns:
        None
    """
    with open(file_path, 'r') as f_read:
        data = f_read.read()
    
    data = data.lower()
    sentences_tokenized = sent_tokenize(data)
    
    # The list we will output to file
    cleaned_data = []
    
    for sentence in sentences_tokenized:
        sentence = re.sub(r'--', ' ', sentence)
        sentence = re.sub(r'[.,;:!?]]', '', sentence)
        sentence = re.sub(r'favour', 'favor', sentence)
        sentence = re.sub(r'endeavour', 'endeavor', sentence)
        sentence = re.sub(r'colour', 'color', sentence)
        sentence = re.sub(r'behaviour', 'behavior', sentence)
        sentence = re.sub(r'possest', 'possessed', sentence)
        sentence = re.sub(r'phaenomen', 'phenomen', sentence)
        
        
        
        


# We compile the Spooky Author's dataset into a single file
