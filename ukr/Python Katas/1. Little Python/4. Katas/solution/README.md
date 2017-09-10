# 4. Katas

## Пояснення Рішення | Класи і файли

## Рішення:

1. Створюємо клас:
```python
class VowelsClass:
  ...
```

2. Створюємо метод конструктор в клас який приймає одну змінну (рядок). У самому конструкторі визначаємо чотири змінних (нашу рядок, лист з голосних і два файли в які будемо записувати наші рядки):
```python
  ...
    def __init__(self,string1):
      self.string1 = string1              # string for edit
      self.vowels = ['a','e','i','o','u'] # list of vowels
      self.file1 = 'with_v.txt'           # file for vowels string
      self.file2 = 'without_v.txt'	    # file for not vowels string
  ...
```


3. Створюємо фунцкцію для запису рядка в файл, яка приймає рядок і назва файлу:

  ```python
    ...
    def add_to_file(self, text, file_name):
        ''' add string to file'''
        f = open(file_name, 'w+')   # open file
        f.write(text)               # add string to file
        f.close()                   # close file
    ...
  ```

4. Створюємо фунцкцію для перетворення рядка в рядок без голосних:
```python
  ...
  def with_vowels(self):
        ''' return string with vowels and save to file '''
  ...      
```
- У самій функції:

  1. Записуємо рядок в нову змінну:
  ```python
    ...
    new_string1 = self.string1
    ...      
  ```
  2. Пробігаємо по всій зміній і видаляємо голосні:
  ```python
    ...
    for letter in new_string1:
            if letter in self.vowels:
                new_string1 = new_string1.replace(letter,'')
    ...      
  ```
  3. Записуємо нашу рядок в файл:
  ```python
    ...
    self.add_to_file(new_string1,self.file1)
    ...      
  ```
  4. Повертаємо нашу рядок:
  ```python
    ...
    return new_string1
    ...      
  ```

5. Створюємо фунцкцію для перетворення рядка в рядок без приголосних, то ж алгоритм дій що з попередній функцією:

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

6. Створюємо метод для принта класу, котрий буде виводить рядок, яка нам потрібна по условмію:

```python
  ...
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
  ...      
```

7. Викликаємо наші класи з певними рядками:

```python
  ...
  # Class part:
  c1 = VowelsClass('some word in on string')
  c2 = VowelsClass('one, two, three, four, five, six, ...')
  c3 = VowelsClass("I'm an independent string")
  ...      
```

8. Принт класов:

```python
  ...
  # Output part:
  print(c1)
  print(c2)
  print(c3))
  ...      
```

На цьому і все.

Якщо вам сподобалася Katas, можете поставити цій репозиторії зірочку це буде мене в подальшому мотивувати на написання подібних Katas для вас
