"""
1) Add the file and topic details.
   a) Mention the file name as `02-steps-at-scale.py`.
   b) Mention the topic as "Time Complexity".
   c) Introduce the program as a way to see how steps grow when `n` becomes bigger.

2) Start with a reminder.
   a) Print that the double loop took 10 steps when `n = 4`.
   b) Use `input()` to pause the program before showing larger values.

3) Create different input sizes.
   a) Use a list with values 10, 100, and 1000.
   b) Use a for loop to test each value of `n`.

4) Pause before each result.
   a) Show the current value of `n`.
   b) Ask the user to press Enter before calculating the steps.

5) Calculate the number of steps.
   a) Use the formula `n * (n + 1) // 2`.
   b) This gives the same step count as the double loop.
   c) Use floor division `//` to keep the result as a whole number.

6) Display the result.
   a) Print the number of steps for each value of `n`.
   b) Help the user see that steps grow very quickly as `n` increases.
"""

# 02-steps-at-scale.py

# Topic: Time Complexity — how steps grow as n gets bigger

# Double Loop at n = 4 took 10 steps. Watch what happens as n grows.

input("Double Loop at n = 4 took 10 steps. Watch it grow. Press Enter ")

for n in [10, 100, 1000]:

  input("n = " + str(n) + " Press Enter ")

print(" steps =", n * (n + 1) // 2)