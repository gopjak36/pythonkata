# 3. Katas

## Пояснення Рішення | Текст без багаточисльних пробілів

## Рішення:
- Перша функція:
  1. Створюємо функцію з двома переменемі для входу (текстом який треба записати і файл для запису), яка буде записувати текс в файл:
  ```python
  def add_text_to_file(text,file):
    '''
    Input: text, file name
    Return: add text to file
    '''
    ...
  ```

  2. У самій функції:
    - Відкриваємо файл для запису:
    ```python
      ...
      f = open(file,"w")  # open file
      ...
    ```
    - Записуємо текст:
    ```python
      ...
      print(text,file=f)  # add text to file#
      ...
    ```
    - Закриваємо файл для запису:
  ```python
    ...
    f.close()           # file close
    ...
  ```
- Друга функція:
  1. Створюємо функцію з однією змінною для входу (файл), яка буде видаляти численні пробіли:
  ```python
    ...
    def delete_multispace(f):
      '''
      Input: some file
      Return: string with multi space
      '''
    ...
  ```
  2. У самій функції:
    - Відкриваємо файл:
    ```python
      ...
      f = open(f,'r')               # open file
      ...
    ```
    - Створюємо змінну для слів у вигляді порожнього словника:
    ```python
      ...
      words_list = []               # empty list for words from file
      ...
    ```
    - Пробігаємо по всіх рядках файлу:
    ```python
      ...
      for string in f:              # go around all lines in file
      ...
    ```
    - Пробігаємо по всіма словами рядка:
    ```python
      ...
        for word in string.split(): # go around all word in line
      ...
    ```
    - Додаємо слово в список для слів:
    ```python
        words_list.append(word)   # add word to list
    ```    
    - Створюємо змінну в яку відразу додаємо всі слова зі списку для слів у вигляді рядка:
    words_list.append(word)   # add word to list
    ```python
      ...
      string = ' '.join(words_list) # add words list to string
      ...
    ```
    - Закриваємо файл:
    ```python
      ...
      f.close()           # file close
      ...
    ```
    - Повертаємо рядок з усіма словами:
    ```python
      ...
      return string
      ...
    ```

  3. Створюємо змінні для файлів:
   - Файл з якого читаємо текст:
   ```python
     ...
     file1 = 'default.txt' # file with multi space
     ...
   ```
   - Файл в який записуємо текст:
   ```python
     ...
     file2 = 'data.txt' # final file
     ...
   ```

  4. Основна частина:
   - Отримуємо рядок зі словами з першого файлу за допомогою функції:
   ```python
     ...
     text = delete_multispace(file1) # get text without multi space from file1
     ...
   ```
   - Додаємо рядок яку отримали в файл для запису в функцію, яка записує в файл:
   ```python
     ...
     add_text_to_file(text,file2) # add text to file 2
     ...
   ```

 На цьому і все.

 Якщо вам сподобалася Katas, можете поставити цій репозиторії зірочку це буде мене в подальшому мотивувати на написання подібних Katas для вас.
