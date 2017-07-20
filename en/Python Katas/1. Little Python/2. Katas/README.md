# 2. Katas

## Outstanding Balance on the Credit Card

## Problem:

Write a program that considers the Outstanding Balance on the Credit Card if you pay only the Minimum Payment for a whole year.

For this, three variables are given to enter the function:

  - __outStandingBalance__ - outstanding balance on credit card.
  - __yearlyPercentRate__ - yearly percent rate.
  - __monthlyPercentRate__ - monthly percent rate.

__Note:__ If you want to know how to calculate the outstanding balance after one month, __See the section below. Example.__

## Task:

Write a function that returns such a string: __"Remaining Outstanding Balance: b"__, where b is the outstanding balance (rounded to the second decimal point) that the function returned.

__!Also__, Prints these lines while the function is running:

```text
  Month 1 Outstanding Balance: b | Minimum payment this month: m
  ...
  Month 1 Outstanding Balance: b | Minimum payment this month: m

  when b - Outstanding Balance, а m - Minimum payment this month.
```

## Example:

To calculate the outstanding balance after one month, one must adhere to such an algorithm:

  1. Consider the minimum payment that we can make in a month:
    - __minPay = outStandingBalance * monthlyPercentRate__
  2. Consider the balance, after the minimum payment:
    - __balanceAfterMinPay = outStandingBalance - minPay__
  3. Consider the percentage that we have to pay for using the card per month:
    - __Percent = (yearlyPercentRate / 12.0) * balanceAfterMinPay__
  4. Consider the outstanding balance at the end of the month:
    - __outStandingBalance = balanceAfterMinPay + Percent__

> Do not forget that we counted only for one month.

## Data to verify:

> creditCardOutStanding - Function name

1. creditCardOutStanding(3329,0.2,0.03) --> __"Remaining Outstanding Balance:  2816.55"__

2. creditCardOutStanding(341,0.12,0.053) --> __"Remaining Outstanding Balance:  207.63"__

3. creditCardOutStanding(168,0.15,0.06) --> __"Remaining Outstanding Balance:  92.81"__

> Where "-->" means after starting the program

## What's next ?

__The program does not come out or works not exactly__, go to the solution folder and look at the explanation for solving the problem, this will help you.

__If you have everything turned out__, you can go to the solution package and compare your solution with the one that's there.

> If your decision does not coincide with my decision, then I'm very happy for you. __Please share it with me, I will be very grateful to you and then I will add it to the solution folder__. How to add your solution, see here
