# 2. Katas

## Непогашений Залишок на Кредитній Картці

## Проблема:

Написати програму, яка рахує Непогашений Непогашений Залишок на Кредитній Картці, якщо цілий рік виплачувати тільки Мінімальний Платіж.

Для цього дається три змінні на вхід в функцію:

  - __outStandingBalance__ -  непогашений залишок на кредитній картці.
  - __yearlyPercentRate__ - річна процентна ставка.
  - __monthlyPercentRate__ -  місячна процентна ставка.

__Примітка:__ Якщо ви хочете дізнатися, як порахувати непогашений залишок після одного місяця, __дивіться в розділі нижче Приклад.__

## Завдання:

Написати функцію, яка повертає такий рядок: __"Непогашений Залишок складає: b"__, где b - непогашений залишок (заокруглений до другої цифри після коми), який повернула функція.

__!Також__, друкує ось такі рядки під час роботи функції:

```text
  Місяць 1 Непогашений Залишок: b | Мінімальний платіж в цьому місяці: m
  ...
  Місяць 12 Непогашений Залишок: b | Мінімальний платіж в цьому місяці: m

  де b - непогашений залишок, а m - мінімальний платіж в цьому місяці.
```

## Приклад:

Щоб порахувати непогашений залишок після одного місяця треба дотримуватися такого алгоритму:

  1. Рахуємо мінімальний платіж, який можна зробити в місяці:
    - __minPay = outStandingBalance * monthlyPercentRate__
  2. Рахуємо залишок, після мінімального платежу:
    - __balanceAfterMinPay = outStandingBalance - minPay__
  3. Рахуємо відсоток, який ми повинні заплатити за використання карти в місяць:
    - __Percent = (yearlyPercentRate / 12.0) * balanceAfterMinPay__
  4. Рахуємо непогашений залишок в кінці місяця:
    - __outStandingBalance = balanceAfterMinPay + Percent__

>Не забувайте що ми порахували тільки для одного місяця.

## Дані для перевірки:

> creditCardOutStanding - назва функції

1. creditCardOutStanding(3329,0.2,0.03) --> __"Непогашений Залишок складає:  2816.55"__

2. creditCardOutStanding(341,0.12,0.053) --> __"Непогашений Залишок складає:  207.63"__

3. creditCardOutStanding(168,0.15,0.06) --> __"Непогашений Залишок складає:  92.81"__

> де "-->" означає після запуску програми

__Примітка:__ Не забувайте що функція, також повинна друкувати рядки під час своєї роботи.

## Що далі ?

__Программа не виходить або працює не зовсім точно__, перейдіть в папку solution і подивіться пояснення до вирішення проблеми, це вам допоможе.

__Якщо у вас все вийшло__, можете перейти в паку solution і порівняти своє рішення з тим яке там є.

> Якщо ваше рішення не збігається з моїм рішення, то я за вас дуже радий. __Поділітся їм зі мною, я буду вам дуже вдячний і тоді я додам його в папку solution__. Як додати своє рішення дивіться тут.