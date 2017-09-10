# 4. Katas

## Объяснение Решения | Классы и файлы

## Решение:

1. Создаем класс:
```python
class VowelsClass:
  ...
```

2. Создаем метод конструктор в класс который принимает одну переменную(строку). В самом конструкторе определяем четыре переменных(нашу строку, лист из гласных и два файла в которые будем записывать наши строки):
```python
  ...
    def __init__(self,string1):
      self.string1 = string1              # string for edit
      self.vowels = ['a','e','i','o','u'] # list of vowels
      self.file1 = 'with_v.txt'           # file for vowels string
      self.file2 = 'without_v.txt'	    # file for not vowels string
  ...
```


3. Создаем функцию для записи строки в файл, которая принимает строку и название файла:

  ```python
    ...
    def add_to_file(self, text, file_name):
        ''' add string to file'''
        f = open(file_name, 'w+')   # open file
        f.write(text)               # add string to file
        f.close()                   # close file
    ...
  ```

4. Создаем функцию для преобразования строки в строку без гласных:
```python
  ...
  def with_vowels(self):
        ''' return string with vowels and save to file '''
  ...      
```
- В самой функции:

  1. Записываем строку в новую переменную:
  ```python
    ...
    new_string1 = self.string1
    ...      
  ```
  2. Пробегаем по всей переменой и удаляем гласные:
  ```python
    ...
    for letter in new_string1:
            if letter in self.vowels:
                new_string1 = new_string1.replace(letter,'')
    ...      
  ```
  3. Записываем нашу строку в файл:
  ```python
    ...
    self.add_to_file(new_string1,self.file1)
    ...      
  ```
  4. Возвращаем нашу строку:
  ```python
    ...
    return new_string1
    ...      
  ```

5. Создаем функцию для преобразования строки в строку без согласных, то же алгоритм действий что из предыдущий функцией:

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

6. Создаем метод для принта класса, котрый будет выводит строку, которая нам нужна по условмию:

```python
  ...
  def __str__(self):
        ''' Output info about class '''

        print('----------------------------------------------------------------')
        return "Строка: '%s' \n Без гласных '%s'; Записана в файл --> '%s'\nБез согласных '%s'; Записана в файл --> '%s'" % (
                                                                                                            self.string1,
                                                                                                            self.with_vowels(),
                                                                                                            self.file1,
                                                                                                            self.without_vowels(),
                                                                                                            self.file2
                                                                                                            )
  ...      
```

7. Вызываем наши классы с определенными строками:

```python
  ...
  # Class part:
  c1 = VowelsClass('some word in on string')
  c2 = VowelsClass('one, two, three, four, five, six, ...')
  c3 = VowelsClass("I'm an independent string")
  ...      
```

8. Принтим классы:

```python
  ...
  # Output part:
  print(c1)
  print(c2)
  print(c3))
  ...      
```

На этом и все.

Если вам понравилась Katas, можете поставить этой репозитории звездочку это будет меня в дальнейшем мотивировать на написание подобных Katas для вас.
