p# 4. Katas

## Classes and files

## Problem:

We have a string in __lower case__, you need to get two lines one with the other's vowels with consonants, which will be written to the files. All this must be done with the help of one class and called in this form:

```python
    print(VowelsClass('some string'))

    # где VowelsClass - class name
```

## Task:

As you understand with the title, your task will be to write a class. Which will convert the string to a string with __vowels__ and separately with __consonants__, and write them to files. Also __With a Print Class__, as shown in the Problem above, it should issue the following text:

```text
    String: 'string'
    Without vowels 'strng'; Write to file --> 'with_vowels.txt'
    Without consonants 'i'; Write to file --> 'without_vowels.txt'
```

## Data to verify:

> VowelsClass() - class name

1. VowelsClass('some word in on string') -->
```text
    String: 'some word in on string'
    Without vowels 'sm wrd in n strng'; Write to file --> 'with_vowels.txt'
    Without consonants 'oe o i o i'; Write to file --> 'without_vowels.txt'
```

2. VowelsClass('one, two, three, four, five, six, ...') -->
```text
    String: 'one, two, three, four, five, six, ...'
    Without vowels 'on, tw, thr, fr, fv, sx, ...'; Write to file --> 'with_vowels.txt'
    Without consonants 'e, o, ee, ou, ie, i, ...'; Write to file --> 'without_vowels.txt'
```

3. VowelsClass('I'm an independent string') -->
```text
    String: 'I'm an independent string'
    Without vowels ''m n ndpndnt strng'; Write to file --> 'with_vowels.txt'
    Without consonants 'I' a ieee i'; Write to file --> 'without_vowels.txt'
```

> Where "-->" means after starting the program

## What's next ?

__The program does not come out or works not exactly__, go to the solution folder and look at the explanation for solving the problem, this will help you.

__If you have everything turned out__, you can go to the solution package and compare your solution with the one that's there.

> If your decision does not coincide with my decision, then I'm very happy for you. __Please share it with me, I will be very grateful to you and then I will add it to the solution folder__. How to add your solution, see here
