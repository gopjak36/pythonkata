# -*- coding: utf-8 -*
''' Class and File  '''

class VowelsClass:

    def __init__(self,string1):
        self.string1 = string1              # string for edit
        self.vowels = ['a','e','i','o','u'] # list of vowels
        self.file1 = 'with_v.txt'           # file for vowels string
        self.file2 = 'without_v.txt'	    # file for not vowels string

    def add_to_file(self, text, file_name):
        ''' add string to file'''
        f = open(file_name, 'w+')   # open file
        f.write(text)               # add string to file
        f.close()                   # close file

    def with_vowels(self):
        ''' return string with vowels and save to file '''
        new_string1 = self.string1

        for letter in new_string1:
            if letter in self.vowels:
                new_string1 = new_string1.replace(letter,'')

        self.add_to_file(new_string1,self.file1)

        return new_string1

    def without_vowels(self):
        ''' return string without vowels and save to file '''
        new_string2 = self.string1

        for letter in new_string2:
            if letter not in self.vowels:
                new_string2 = new_string2.replace(letter,'')

        self.add_to_file(new_string2,self.file2)

        return new_string2

    def __str__(self):
        ''' Output info about class '''

        print('----------------------------------------------------------------')
        return "Рядок: '%s'\nБез голосних '%s'; Записана в файл --> '%s' Без приголосних '%s'; Записана в файл --> '%s" % (
                                                                                                            self.string1,
                                                                                                            self.with_vowels(),
                                                                                                            self.file1,
                                                                                                            self.without_vowels(),
                                                                                                            self.file2
                                                                                                            )


# Class part:
c1 = VowelsClass('some word in on string')
c2 = VowelsClass('one, two, three, four, five, six, ...')
c3 = VowelsClass("I'm an independent string")

# Output part
print(c1)
print(c2)
print(c3)
