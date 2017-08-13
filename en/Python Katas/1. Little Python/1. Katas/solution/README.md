# 1. Katas

## Explanation of the Solution | How many bobs are there?

1. Create variables for work:

  - s, the string you want to check.

  - count = 0, the counter to navigate to how the stage is now located. This means that if count = 1, then we know that we have " b _ _ ", if count = 2, then " b o _ " and if count = 3, then " b o b ".

  - bob = 0, the number of bob are occurs.

2. Let's go to the main part of the program:

  - To go over all the elements of the string s, and letter is our current letter in the string s. We use:

```python
for letter in s:
  ...
```

  - We check what kind of current letter and meter we have. From the very beginning, we indicated that the counter is 0. And now, for example, if we hit the letter "b" and our counter is 0, we add to the counter +1, so that when the next letter is received, the program understands that we already have First "b". If the next letter we get on the letter "o", we add +1 to the counter and the program understands that now we have "bo". And then if the next letter to which we get is the letter "b", then we add to the variable bob +1 as we understand that now we have the string "... bob ..." in a row and change the counter value to 1 as well How it can beat the beginning of another bobs, you remember what was written in the note. Let's see another example, when the counter is 1 and the current letter is not equal to "o", then we go to __else__, as it works we look at the next paragraph.

```python
...
  if count == 0 and letter == 'b':
      count = 1

  elif count == 1 and letter == 'o':
      count = 2

  elif count == 2 and letter == 'b':
      count = 3
      bob + = 1
      count = 1

  else:
    ...
```
  - Here we check that the current letter is "b" and the counter is 1, since each "b" can beat the beginning of a new bobs. In another case, we simply cancel our counter.

```python
...
  else:
        if letter == 'b' and letter == 1:
            pass
        else:
            count = 0
  ...
```

3. At the very end of the introduction, what was required of us:
```python
...
print ('Bob occurs times:', bob)
```

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
