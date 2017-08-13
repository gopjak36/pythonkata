# 2. Katas

## Explanation of the Solution | Minimum Pay for Credit Card

## Solution:

1. Create a function that takes two variables.

2. We pass to a part of the help variables:

  - __start_balance__ - to duplicate the outstanding balance, later it will come in handy.
  - __minPay__ - the minimum payment at the moment, can and will approach ;)
  - __count__ - for the number of attempts for which the program has found the minimum payment.


3. We pass to the main part of the program:

  - We will use the cycle __while__, since we do not know how many attempts we will need.

  - Help variables in the cycle itself:

    - __month__ - zero the month to the starting value.
    - __OutStandingBalance__ - zero the outstanding balance to the starting value.
    - __count__ - add 1 to the number of attempts.

  - We apply the algorithm that we disassembled in the Example to calculate the outstanding balance after the year of payment by only a minimum payment.

  - We check the outstanding balance after one year:

    - ЕIf it is equal to or less than 0, then this means that __minPay__ is matched correctly and we return a string by condition.
    - In other cases, adds __minPay__ 10 and start 3 point again.

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
