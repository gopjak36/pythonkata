# 2. Katas

## Объяснение Решения | Текст без многочисленных пробелов

## Решение:
- Первая функция:
  1. Создаем функцию с двумя переменеми для входа(текстом который надо записать и файл для записи), которая будет записывать текс в файл:
  ```python
  def add_text_to_file(text,file):
    '''
    Input: text, file name
    Return: add text to file
    '''
    ...
  ```

  2. В самой функции:
    - открываем файл для записи:
    ```python
      ...
      f = open(file,"w")  # open file
      ...
    ```
    - записываем текст:
    ```python
      ...
      print(text,file=f)  # add text to file#
      ...
    ```
    - закрываем файл для записи:
  ```python
    ...
    f.close()           # file close
    ...
  ```
- Вторая функция:
  1. Создаем функцию с одной переменой для входа(файл), которая будет удалять многочисленные пробелы:
  ```python
    ...
    def delete_multispace(f):
      '''
      Input: some file
      Return: string with multi space
      '''
    ...
  ```
  2. В самой функци:
    - Открываем файл:
    ```python
      ...
      f = open(f,'r')               # open file
      ...
    ```
    - Создаем переменную для слов в виде пустого словаря:
    ```python
      ...
      words_list = []               # empty list for words from file
      ...
    ```
    - Пробегаем по всем строкам файла:
    ```python
      ...
      for string in f:              # go around all lines in file
      ...
    ```
    - Пробегаем по всем словам строки:
    ```python
      ...
        for word in string.split(): # go around all word in line
      ...
    ```
    - Добавляем слово в список для слов:
    ```python
        words_list.append(word)   # add word to list
    ```    
    - Создаем переменную в которую сразу добавляем все слова из списка для слов в виде строки:
    words_list.append(word)   # add word to list
    ```python
      ...
      string = ' '.join(words_list) # add words list to string
      ...
    ```
    - Закрываем файл:
    ```python
      ...
      f.close()           # file close
      ...
    ```
    - Возвращаем строку со всеми словами:
    ```python
      ...
      return string
      ...
    ```

  3. Создаем переменные для файлов:
   - Файл с которого чисатем текст:
   ```python
     ...
     file1 = 'default.txt' # file with multi space
     ...
   ```
   - Файл в который записываем текст:
   ```python
     ...
     file2 = 'data.txt' # final file
     ...
   ```

  4. Основная часть:
   - Получаем строку со словами из первого файла с помощью функции:
   ```python
     ...
     text = delete_multispace(file1) # get text without multi space from file1
     ...
   ```
   - Добавляем строку которую получили в файл для записи в функцию, которая записывает в файл:
   ```python
     ...
     add_text_to_file(text,file2) # add text to file 2
     ...
   ```
   
На этом и все.

Если вам понравилась Katas, можете поставить этой репозитории звездочку это будет меня в дальнейшем мотивировать на написание подобных Katas для вас.
