# 4. Katas

## Explanation of the Solution | Classes and files

## Solution:

1. Create class:
```python
class VowelsClass:
  ...
```

2. Create a constructor method in a class that takes one variable (a string). In the constructor itself, we define four variables (our string, a sheet of vowels and two files into which we will write our lines):
```python
  ...
    def __init__(self,string1):
      self.string1 = string1              # string for edit
      self.vowels = ['a','e','i','o','u'] # list of vowels
      self.file1 = 'with_v.txt'           # file for vowels string
      self.file2 = 'without_v.txt'	    # file for not vowels string
  ...
```


3. Create a function to write a string to a file that takes a string and a file name:

  ```python
    ...
    def add_to_file(self, text, file_name):
        ''' add string to file'''
        f = open(file_name, 'w+')   # open file
        f.write(text)               # add string to file
        f.close()                   # close file
    ...
  ```

4. Create a function to convert a string to a string without vowels:
```python
  ...
  def with_vowels(self):
        ''' return string with vowels and save to file '''
  ...      
```
- In the function:

  1. Write a string to a new variable:
  ```python
    ...
    new_string1 = self.string1
    ...      
  ```
  2. We run through the whole change and delete the vowels:
  ```python
    ...
    for letter in new_string1:
            if letter in self.vowels:
                new_string1 = new_string1.replace(letter,'')
    ...      
  ```
  3. Write our string to a file:
  ```python
    ...
    self.add_to_file(new_string1,self.file1)
    ...      
  ```
  4. Returning our string:
  ```python
    ...
    return new_string1
    ...      
  ```

5. Create a function for converting a string to a string without consonants, the same action algorithm as the previous function:

```python
  ...
  def without_vowels(self):
        ''' return string without vowels and save to file '''
        new_string2 = self.string1

        for letter in new_string2:
            if letter not in self.vowels:
                new_string2 = new_string2.replace(letter,'')

        self.add_to_file(new_string2,self.file2)

        return new_string2
  ...      
```

6. We create a method for printing a class that will print a string that we need by convention:

```python
  ...
  def __str__(self):
        ''' Output info about class '''

        print('----------------------------------------------------------------')
        return "String: '%s' \nWithout vowels '%s'; Write to file --> '%s'\nWithout consonants '%s'; Write to file --> '%s'" % (
                                                                                                            self.string1,
                                                                                                            self.with_vowels(),
                                                                                                            self.file1,
                                                                                                            self.without_vowels(),
                                                                                                            self.file2
                                                                                                            )
  ...      
```

7. We call our classes with certain strings:

```python
  ...
  # Class part:
  c1 = VowelsClass('some word in on string')
  c2 = VowelsClass('one, two, three, four, five, six, ...')
  c3 = VowelsClass("I'm an independent string")
  ...      
```

8. Print classes:

```python
  ...
  # Output part:
  print(c1)
  print(c2)
  print(c3))
  ...      
```

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
