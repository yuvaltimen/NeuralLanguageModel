"""
Text to CSV of sentences. 

Open file. 
lines = Read in lines.

for each line:
Split by . ! ? and trim.
add to sentences.

for each sentence:
pair with ID. 

Write to file. 

"""

import os
import re

def load_word_list(filename):
  """
  (This function is borrowed from the Lecture 5 Jupyter notebook,
  with slight modifications.)

  Loads a lexicon from a plain text file in the format of one word per line.
  Parameters:
  filename (str): path to file

  Returns:
  list: list of words
  """

  with open(filename, 'r') as f:
      # read the lines into a list
      return [line.strip() for line in f]
  # otherwise display error and return an empty list
  print("load_word_list: problem opening file '{}'".format(filename))
  return []


def append_sentences_to_file(string_list, target_file="nietzsche_sentences.txt"):
  """
  Split the strings into separate sentences. 
  - Remove blank strings
  - Remove lines representing chapter headings
  - Remove lines with just numbers: 1. or [roman numeral].
  Write (append) the sentences list to the end of the target file. 
  """
  with open(target_file, 'a') as f:
    for line in string_list:

      if line.strip() == "":
        continue

      if is_chapter_header(line):
        continue

      if is_end_of_book(line):
        return

      # Split on sentence boundaries . ! ?
      for sentence in re.split("[\\.\\!\\?]", line):
        if sentence.strip() == "":
          continue
        f.write(sentence) 
        f.write('\n')


def is_chapter_header(line):
  # check if a line is a chapter header.
  # 1. Text includes one of: 
  #   PREFACE , CHAPTER , NOTE, TRANSLATOR, d+ , roman numeral
  # 2. Line is then assumed to be chapter heading if it is <50 chars. 
  header_pattern = "(PREFACE|CHAPTER|NOTE|TRANSLATOR|[IVX]+|[ivx]+|\\d+)"
  header_char_limit = 50
  return re.search(header_pattern, line) != None and len(line) < header_char_limit

### Tests - is_chapter_header ###
# print(is_chapter_header("PREFACE: lksdfj"))
# print(is_chapter_header("Chapter I."))
# print(is_chapter_header("IXVIX"))
# print(is_chapter_header("34. "))
# print(is_chapter_header("chapter"))
# print(is_chapter_header("1. If zero or more characters at the beginning of string match the r"))
    

def is_end_of_book(line):
  end_text_1 = "End of the Project Gutenberg"
  end_text_2 = "End of this Project Gutenberg"
  end_pattern = "({}|{}|{}|{}|{}|{})".format(end_text_1, end_text_1.lower(), end_text_1.upper(), \
    end_text_2, end_text_2.lower(), end_text_2.upper())
  return re.search(end_pattern, line) != None

if __name__ == '__main__':
  basepath = 'preface_stripped/'
  for entry in os.listdir(basepath):
    path = os.path.join(basepath, entry)
    if os.path.isfile(path):
      print(entry)
      append_sentences_to_file(load_word_list(path))