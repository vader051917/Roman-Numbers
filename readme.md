# Roman Numbers

**This repository contains a python code file to generate numbers into roman numbers of any number between 1 and 3,999,999.**

The list `ls` contains the list of numbers for which correspong to a specified roman character.
It contains values _1, 5, 10, 50, 100, 500, 1000_.

-   Using `find_pos`, we finds the next smallest element `least_val` and next largest element `max_val` from list `ls` for a given number. 

-   We divide the given number with least value and take the quotient in variable `multiple` and the remainder in variable `remainder`.

-   There are 2 categories which are treated differently:

    * If least value is contains 1s, i.e. it can take values 1, 10, 100 and 1000.
        
    * Other category is when least value contains 5s, i.e. it can take values 5, 50 and 500.
