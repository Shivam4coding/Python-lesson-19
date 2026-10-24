"""
1) Add the file and topic details.
   a) Mention the file name as `03-list-in-memory.py`.
   b) Mention the topic as "Space Complexity".
   c) Introduce the program as a way to see how list memory grows with `n`.

2) Set the starting value.
   a) Store 4 in the variable `n`.
   b) Use this value for the first memory example.

3) Ask the user to predict.
   a) Ask how many items the list will store when `n = 4`.
   b) Store the user's guess in the `guess` variable.

4) Create the list.
   a) Use `range(1, n + 1)` to create numbers from 1 to `n`.
   b) Convert the range into a list using `list()`.
   c) Store the list in `points`.

5) Display the list memory use.
   a) Print the user's guess.
   b) Print the full list.
   c) Use `len(points)` to show how many items are stored.

6) Show growth at larger sizes.
   a) Ask the user to think about what happens as `n` grows.
   b) Use a for loop to test sizes 4, 10, 100, and 1000.
   c) Print how many items the list stores for each size.

7) Highlight the space complexity idea.
   a) Explain that the list keeps every item in memory.
   b) Show that memory grows as `n` grows.
"""

# 03-list-in-memory.py

# Topic: Space Complexity — how much memory an algorithm uses

# List stores every score in memory, so memory grows as n grows (On space)

n = 4

# List stores every score in memory — memory grows with n

guess = input("Predict: how many items in the List for n = 4? ")
points = list(range(1, n + 1))

print(" your guess:", guess, " List:", points, " items:", len(points))
input("Predict: what happens to List size as n grows? Press Enter ")

for size in [4, 10, 100, 1000, 10000]:
  print(f"n = {size:<5} List uses {size:>5} items in memory")