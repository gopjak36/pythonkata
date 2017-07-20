# 2. Katas

## Explanation of the Solution | Outstanding Balance on the Credit Card

## Solution:

1. Create a function that takes three variables:
```python
def creditCardOutStanding(outStandingBalance, yearlyPercentRate, monthlyPercentRate):
  ...
```

2. Create a variable __month__ for the calculation of months, with a value of 1, since we will start from the first month:
```python
  ...
  month = 1
  ...
```
3. We pass to the main part of the program:

  - We will use the cycle __while__ to run through all the months (from 1 to 12):
  ```python
    ...
    while month < 13:
    ...
  ```

  - We consider the outstanding balance after one month and round each time to the second decimal point for a more accurate result:
  ```python
    ...
    while month < 13:
      minPay = round(outStandingBalance * monthlyPercentRate,2)
      balanceAfterMinPay = round(outStandingBalance - minPay,2)
      percent = round((yearlyPercentRate/12.0)*balanceAfterMinPay,2)
      outStandingBalance = round(balanceAfterMinPay + percent,2)
    ...
  ```

  - Display the line (by condition) and add to our variable month 1 to go to the next month:
  ```python
    ...
    outStandingBalance = round(balanceAfterMinPay + percent,2)
    print('Month '+str(month)+' Outstanding Balance: '+str(outStandingBalance) + ' | Minimum payment this month: ' + str(minimunPayment))
    month +=1
    ...
  ```

4. In the final part, we return a string that is given to us by condition:
```python
  ...
  while month < 13:
  ...
  return "Remaining Outstanding Balance: " + str(outStandingBalance)
```

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
