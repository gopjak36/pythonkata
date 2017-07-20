# 2. Katas

## Explanation of the Solution | Minimum Payment for a Credit Card using Binary Search

## Solution:

1. Create a function that takes two variables.

2. We pass to a part of the help variables:

  - __start_balance__ - to duplicate the outstanding balance, later it will come in handy.
  - __monthlyPercentRate__ - monthly percent rate.
  - __lowerPay__ - lower limit of payment.
  - __upperPay__ - upper limit of payment.
  - __epsilon__ - comparison variable.
  - __count__ - for the number of attempts for which the program has found the minimum payment.

3. We pass to the main part of the program:

  - We will use the cycle __while__, since we do not know how many attempts we will need.

  - Help variables in the cycle itself:

    - __minPay__ - minimum payment at the moment.
    - __OutStandingBalance__ - original outstanding balance.
    - __count__ - add 1 to the number of attempts.

  - Apply the algorithm, which we disassembled in Example.

  - Check the outstanding balance after one year:

    - If it is larger than __epsilon__, then we change the lower limit to __minPay__ and we return to item 3.
    - If it is smaller than __epsilon__, then we change the upper limit to __minPay__ and we return to item 3.
    - In other cases, we exit the cycle.

4. Round __minPay__ up to the second digit after the comma and return the string by condition.    

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you..
