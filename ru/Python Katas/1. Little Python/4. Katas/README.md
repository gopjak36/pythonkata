# 4. Katas

## Классы и файлы

## Проблема:

У нас есть строка в __нижнем регистре__, нужно получить две строки одна с гласными другая с согласными, которые будут записываться в файлы. Все это надо сделать с помощью одного класса и вызывать в таком виде:

```python
    print(VowelsClass('some string'))

    # где VowelsClass - название класса
```

## Задача:

Как вы поняли с название, ваша задача будут написать класс. Который будет преобразовать строку в строку с __гласными__ и отдельно с __согласными__, и записать их в файлы. К тому же __При Принте Класса__, как показано в Проблеме выше она должна выдавать такой текст:

```text
    Строка: 'string'
    Без гласных 'strng'; Записана в файл --> 'with_vowels.txt'
    Без согласных 'i'; Записана в файл --> 'without_vowels.txt'
```

## Данные для проверки:

> VowelsClass() - название класса

1. VowelsClass('some word in on string') -->
```text
    Строка: 'some word in on string'
    Без гласных 'sm wrd in n strng'; Записана в файл --> 'with_vowels.txt'
    Без согласных 'oe o i o i'; Записана в файл --> 'without_vowels.txt'
```

2. VowelsClass('one, two, three, four, five, six, ...') -->
```text
    Строка: 'one, two, three, four, five, six, ...'
    Без гласных 'on, tw, thr, fr, fv, sx, ...'; Записана в файл --> 'with_vowels.txt'
    Без согласных 'e, o, ee, ou, ie, i, ...'; Записана в файл --> 'without_vowels.txt'
```

3. VowelsClass('I'm an independent string') -->
```text
    Строка: 'I'm an independent string'
    Без гласных ''m n ndpndnt strng'; Записана в файл --> 'with_vowels.txt'
    Без согласных 'I' a ieee i'; Записана в файл --> 'without_vowels.txt'
```

> где "-->" означает после запуска программы

## Что дальше ?

__Программа не выходит или работает не совсем точно__, перейдите в папку solution и помотрите объяснение к решению проблемы, это вам поможет.

__Если у вас все вышло__, можете перейти в паку solution и сравнить свое решение с тем которое там есть.

> Если ваше решение не совпадает с моим решение, то я за вас очень рад. __Поделитесь им со мной, я буду вам очень боагодарен и тогда я добавлю его в папку solution__. Как добавить свое решение смотрите тут.
