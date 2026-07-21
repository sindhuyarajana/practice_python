# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()


# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

# 1. What does each row represent?

# That's the outer loop (i).

# 2. What should be printed inside that row?

# That's the inner loop (j).

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end="")
#     print()

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()

# Rule of thumb for pattern questions

# Ask yourself:

# What changes every row? → Usually i (outer loop).
# How many times should it be printed? → Controlled by the inner loop.
# What should I print? → Sometimes i, sometimes j, sometimes "*", depending on the pattern.
# letter = "ABCDE"
# for i in range(1, 6):
#     for j in range(i):
#         print(chr(65 + j), end="")
#     print()

rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
