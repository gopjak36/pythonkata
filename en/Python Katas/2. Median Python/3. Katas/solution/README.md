# 3. Katas

## Explanation of the Solution | Search for products in a file

## Solution:

- First function:
  1. Create a function with one variable to enter (file name), which will convert the text of the file into a convenient format to see the list.

  2. In the function itself:
    - open the file.

    - Declare auxiliary variables.

    - We run through the entire file and add the lines to the list and more to the list, making a list in the list.

    - close the file.

    - return the list with the data.

- Second function:
  1. Create a function with two variables to enter (the name of the product we are looking for and the name of the file), which will return all the necessary data for the search for the goods.

  2. In the function itself:

    - Call the first function to get the necessary data from the file as a list.

    - Declare auxiliary variables in which we will write down all the necessary information.

    - We run through the list and search for the name of the product, which must be found and remember the necessary data.

    - Return the tuple with three variables.

  3. Create a variable for the file from which we will read the information.

- Main part:
   1. Create a variable to enter the name of the product for search.

   2. And one more change in which we write down our second function.

- Final printing:

    1. We turn the list of countries into one line for printing.

    2. Print the required row by condition.

That's all.

If you liked Katas, you can put star on this repositories, this will motivate me to write similar Katas for you.
