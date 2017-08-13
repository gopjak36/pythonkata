# 1. Katas

## Explanation of the Solution | Guess number

0. Create a random number:

  - We import the pendon random module:

  - create a random number in the range from 0 to 100:

  - we deduce this random number on a screen that in the end to check the answer.

1. Create variables for work:

  - low_number, lower bound of search.

  - hight_number, the upper limit of the search.

  - count, the number of entries in the program.

2. Let's go to the main part of the program:

  - 1) We use the __while__ loop, since we do not know how many inputs to the program we need.

  - 2) We are looking for an average boundary, the lower and upper boundaries

  - 3) Check whether the average boundary is equal to our random number.

  - 4) If yes, then show on the screen what was asked of us.

  - 5) If not, we change our borders:
      - If the average boundary is greater than the random number, then the upper boundary equals the middle boundary.
      - If the average border is less than the random number, then the lower boundary equals the middle boundary.

  - 6) We return to ii) the point, until iv) is fulfilled.

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
