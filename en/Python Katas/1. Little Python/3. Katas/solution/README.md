# 3. Katas

## Explanation of the Solution | Text without multiple spaces

## Solution:

- The first function:
  1. Create a function with two variables to enter (the text you want to write and the file to write), which will write the text to the file:
  ```python
  def add_text_to_file(text,file):
    '''
    Input: text, file name
    Return: add text to file
    '''
    ...
  ```

  2. In the function:
    - Open the file for writing:
    ```python
      ...
      f = open(file,"w")  # open file
      ...
    ```
    - Write down the text:
    ```python
      ...
      print(text,file=f)  # add text to file#
      ...
    ```
    - Close the file for writing:
  ```python
    ...
    f.close()           # file close
    ...
  ```
- The second function:
  1. Create a function with one variable to enter (file), which will remove multiple spaces:
  ```python
    ...
    def delete_multispace(f):
      '''
      Input: some file
      Return: string with multi space
      '''
    ...
  ```
  2. In the function:
    - Open the file:
    ```python
      ...
      f = open(f,'r')               # open file
      ...
    ```
    - Create a variable for words in the form of an empty dictionary:
    ```python
      ...
      words_list = []               # empty list for words from file
      ...
    ```
    - We run through all the lines of the file:
    ```python
      ...
      for string in f:              # go around all lines in file
      ...
    ```
    - We run through all the words of the line:
    ```python
      ...
        for word in string.split(): # go around all word in line
      ...
    ```
    - Adding a word to the list for words:
    ```python
        words_list.append(word)   # add word to list
    ```    
    - Create a variable in which we immediately add all words from the list for words in the form of a string:
    ```python
      ...
      string = ' '.join(words_list) # add words list to string
      ...
    ```
    - Close the file:
    ```python
      ...
      f.close()           # file close
      ...
    ```
    - Return a string with all the words:
    ```python
      ...
      return string
      ...
    ```

  3. Create variables for files:
   - The file from which we read the text:
   ```python
     ...
     file1 = 'default.txt' # file with multi space
     ...
   ```
   - The file into which we write the text:
   ```python
     ...
     file2 = 'data.txt' # final file
     ...
   ```

  4. Main part:
   - We get a string with words from the first file using the function:
   ```python
     ...
     text = delete_multispace(file1) # get text without multi space from file1
     ...
   ```
   - We add a line that we got to a file for writing to a function that writes to a file:
   ```python
     ...
     add_text_to_file(text,file2) # add text to file 2
     ...
   ```

 That's all.

 If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
