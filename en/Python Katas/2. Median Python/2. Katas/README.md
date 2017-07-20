# 2. Katas

## Minimum Pay for Credit Card

## Problem:

Write a program that considers the Minimum Payment for a Credit Card. Which will pay off the outstanding balance, if you pay it every month for a year.

__Note:__ Minimum Payment is a fixed amount for all 12 months.

For this, two variables are given to enter the function:

 - __outStandingBalance__ - outstanding balance on credit card.
 - __yearlyPercentRate__ - yearly percent rate.

 __Note:__ If you want to know how to calculate the outstanding balance after one month without a monthly percent rate , __See the section below. Example.__

## Task:

Write a function that returns such a string: __"Minimum Payment every month: b | Count used: c"__, where b is the outstanding balance (rounded to the second decimal point) that the function returned and c is the number of attempts the function used to find the minimum payment.

## Example:

To find the outstanding balance after one month without a monthly interest rate, you need to adhere to an algorithm that I described in detail in 2.Katas (Little Python), follow the link and see.

All you have to do is pick up __minPay__ For the already known algorithm.

__Note:__ Try to start with 0 and increase each time by 10 , until __minPay__ will not work.

## Data to verify:

> creditCardLowPay - function name

1. creditCardLowPay(5123,0.2) --> __"Minimum Payment every month: 470 | Count used: 47"__

2. creditCardLowPay(11,0.18) --> __"Minimum Payment every month: 10 | Count used: 1"__

3. creditCardLowPay(858,0.2) --> __"Minimum Payment every month: 80 | Count used: 8"__

> where "-->" means after starting the program

## What's next ?

__The program does not come out or works not exactly__, go to the solution folder and look at the explanation for solving the problem, this will help you.

__If you have everything turned out__, you can go to the solution package and compare your solution with the one that's there.

> If your decision does not coincide with my decision, then I'm very happy for you. __Please share it with me, I will be very grateful to you and then I will add it to the solution folder__. How to add your solution, see here
