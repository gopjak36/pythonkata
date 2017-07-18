# 2. Katas

## Объяснение Решения | Непогашенный Остаток на Кредитной Карте

1. Создаем функцию, которая принимает три переменные:
```python
def creditCardOutStanding(outStandingBalance, yearlyPercentRate, monthlyPercentRate):
  ...
```

2. Создаем переменную __month__ для подчета месяцев, со значением 1, так как начнем с первого мессяца:
```python
  ...
  month = 1
  ...
```
3. Переходим к основной части программы:

  - Будем использовать цикл __while__ чтобы пробегать по всем месяцам(от 1 до 12):
  ```python
    ...
    while month < 13:
    ...
  ```

  - Считаем непогашеный остаток после одного месяца и каждый раз  округляем до второго знака после запятой для более точного результата:
  ```python
    ...
    while month < 13:
      minPay = round(outStandingBalance * monthlyPercentRate,2)
      balanceAfterMinPay = round(outStandingBalance - minPay,2)
      percent = round((yearlyPercentRate/12.0)*balanceAfterMinPay,2)
      outStandingBalance = round(balanceAfterMinPay + percent,2)
    ...
  ```

  - Выводим на экран строку(по условию) и прибавляем к нашей переменной month 1 чтобы перейти на следующий месяц:
  ```python
    ...
    outStandingBalance = round(balanceAfterMinPay + percent,2)
    print('Месяц '+str(month)+' Непогашенный Остаток: '+str(outStandingBalance) + ' | Минимальный Платеж в этом месяце: ' + str(minimunPayment))
    month +=1
    ...
  ```

4. В финальной части возвращаем строку, которая задана нам по условию:
```python
  ...
  while month < 13:
  ...
  return "Непогашенный Остаток составляет: " + str(outStandingBalance)
```
На этом и все.

Если вам понравилась Katas, можете поставить этой репозитории звездочку это будет меня в дальнейшем мотивировать на написание подобных Katas для вас.
