# -*- coding: utf-8 -*
''' Delete Multi Space  '''

# First function - Add Text to File
def add_text_to_file(t,f):
  '''
  Input: text, file name
  Return: add text to file
  '''
  f = open(f,"w")  # open file
  print(t,file=f)  # add text to file
  f.close()           # file close

# Second function - Delete all Multi Space in File
def delete_multispace(f):
  '''
  Input: some file
  Return: string with multi space
  '''
  f = open(f,'r')               # open file
  words_list = []               # empty list for words from file
  for string in f:              # go around all lines in file
    for word in string.split(): # go around all word in line
      words_list.append(word)   # add word to list
  string = ' '.join(words_list) # add words list to string
  f.close()                     # file close
  return string

# files variables:
file1 = 'default.txt' # file with multi space

file2 = 'data.txt' # final file

# main part:
text = delete_multispace(file1) # get text without multi space from file1

add_text_to_file(text,file2) # add text to file 2
