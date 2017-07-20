# 2. Katas

## Пояснення Рішення | Непогашений Залишок на Кредитній Картці

## Рішення:

1. Створюємо функцію, яка приймає три змінні:
```python
def creditCardOutStanding(outStandingBalance, yearlyPercentRate, monthlyPercentRate):
  ...
```

2. Створюємо змінну __month__ для підрахунку місяців, із значенням 1, так як почнемо з першого місяця:
```python
  ...
  month = 1
  ...
```
3. Переходимо до основної частини програми:

  - Будемо використовувати цикл __while__ щоб пробігати по всім місяцям (від 1 до 12):
  ```python
    ...
    while month < 13:
    ...
  ```

  - Рахуємо непогашений залишок після одного місяця і кожного разу округляем до другого знака після коми для більш точного результату:
  ```python
    ...
    while month < 13:
      minPay = round(outStandingBalance * monthlyPercentRate,2)
      balanceAfterMinPay = round(outStandingBalance - minPay,2)
      percent = round((yearlyPercentRate/12.0)*balanceAfterMinPay,2)
      outStandingBalance = round(balanceAfterMinPay + percent,2)
    ...
  ```

  - Виводимо на екран рядок (за умовою) і додаємо до нашої змінної month 1, щоб перейти на наступний місяць:
  ```python
    ...
    outStandingBalance = round(balanceAfterMinPay + percent,2)
    print('Місяць '+str(month)+' Непогашений Залишок: '+str(outStandingBalance) + ' | Мінімальний платіж в цьому місяці: ' + str(minimunPayment))
    month +=1
    ...
  ```

4. У фінальній частині повертаємо рядок, який заданий нам за умовою:
```python
  ...
  while month < 13:
  ...
  return "Непогашений Залишок складає: " + str(outStandingBalance)
```

На цьому і все.

Якщо вам сподобалася Katas, можете поставити цій репозиторії зірочку це буде мене в подальшому мотивувати на написання подібних Katas для вас
