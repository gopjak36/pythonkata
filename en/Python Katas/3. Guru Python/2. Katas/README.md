# 2. Katas

## Minimum Payment for a Credit Card using Binary Search  

## Problem:

Write a program that considers the Minimum Payment for a Credit Card. Which will pay off the outstanding balance, if you pay it every month for a year. __Using Binary Search__

__Note:__ Minimum Payment is a fixed amount for all 12 months.

For this, two variables are given to enter the function:

 - __outStandingBalance__ - Outstanding balance on credit card.
 - __yearlyPercentRate__ - Annual interest rate.

__Note:__ If you want to know how to calculate the outstanding balance after one month, __See the section below. Example.__

## Task:

Write a function that returns such a string: __"Minimum Payment every month: b | Count used: c"__, where b is the outstanding balance (rounded to the second decimal point) that the function returned and c is the number of attempts the function used to find the minimum payment.

## Example:

To find the outstanding balance after one month, you need to adhere to such an algorithm:

  1. Calculate monthly percent rate:
    - __monthlyPercentRate = yearlyPersentRate/12__
  2. Calculate lower and upper limit:
    - __lowerPay = start_balance/12__
    - __upperPay = (start_balance * (1 + monthlyPercentRate)**12)/12.0__
  3. Calculate the minimum payment we can make in a month:
    - __minPay = (upperPay + lowerPay)/2__

  4. Calculate the outstanding balance for one action. For an extensive solution, see [2.Katas (Little Python)](https://github.com/gopjak36/pythonkata/tree/master/en/Python%20Katas/1.%20Little%20Python/2.%20Katas#example), following the link:
    - __utStandingBalance = outStandingBalance - minPay + ((outStandingBalance - minPaye) * monthlyPercentRate)__

__Note:__ The main part of the Binary search algorithm, it's up to you.

## Data to verify:

> creditCardMinPay_BS - function name.

1. creditCardMinPay_BS(320000,0.2) --> __"Minimum Payment every month: 29157.09 | Count used: 17"__

2. creditCardMinPay_BS(999999,0.18) --> __"Minimum Payment every month: 90325.02 | Count used: 22"__

3. creditCardMinPay_BS(999999,0.18) --> __"Minimum Payment every month: 32809.62 | Count used: 20"__

> where "-->" means after starting the program

__Note:__ For comparison, you can run one of the values using the program that we did in [2.Katas (Median Python)](https://github.com/gopjak36/pythonkata/tree/master/en/Python%20Katas/2.%20Median%20Python/2.%20Katas). __Algorithms is power?__

## What's next ?

__The program does not come out or works not exactly__, go to the solution folder and look at the explanation for solving the problem, this will help you.

__If you have everything turned out__, you can go to the solution package and compare your solution with the one that's there.

> If your decision does not coincide with my decision, then I'm very happy for you. __Please share it with me, I will be very grateful to you and then I will add it to the solution folder__. How to add your solution, see here
