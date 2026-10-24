"""
1) Add the file and topic details.
   a) Mention the file name as `01-three-algorithms.py`.
   b) Mention the topic as "Algorithms".
   c) Introduce the program as three ways to solve the same problem.

2) Set the contest size.
   a) Store the number of students in `n`.
   b) Use 4 students for the example.

3) Ask the user to guess.
   a) Show the points as 1 + 2 + 3 + 4.
   b) Ask the user to enter the total points.

4) Solve using the formula method.
   a) Pause the program until the user presses Enter.
   b) Use the formula `n * (n + 1) // 2`.
   c) Print the total.
   d) Show that this method takes 1 step.

5) Solve using the loop method.
   a) Reset `total` to 0.
   b) Use a for loop from 1 to `n`.
   c) Add one student's points at a time.
   d) Print the total and number of steps.

6) Solve using the double loop method.
   a) Reset `total` and `steps` to 0.
   b) Use an outer loop for each student.
   c) Use an inner loop to count each point.
   d) Increase `total` and `steps` by 1 each time.

7) Compare the three methods.
   a) Show that all methods give the same total.
   b) Show that the number of steps is different.
   c) Print the user's original guess at the end.
"""

# 01-three-algorithms.py

# Topic: Algorithms — three ways to solve the same problem (Formula, Loop, Double Loop)

# Same answer every time, but the number of steps is different

# 4 students in a contest: student 1 earns 1 pt, student 2 earns 2 pts, student 3 earns 3 pts, student 4 earns 4 pts

n = 4

guess = input("Total points: 1 + 2 + 3 + 4 = ")
input("Formula: one calculation. Press Enter to run ")
total = n * (n + 1) // 2

print(" total =", total, " steps = 1")
input("Loop: adds one student at a time. Press Enter to run ")
total = 0

for student in range(1, n + 1):

   total += student

print(" total =", total, " steps =", n)
input("Double Loop: counts every single point. Press Enter to run ")
total = 0
steps = 0

for student in range(1, n + 1):

  for point in range(1, student + 1):

   total += 1

steps += 1
print(" total =", total, " steps =", steps, " your guess was:", guess)