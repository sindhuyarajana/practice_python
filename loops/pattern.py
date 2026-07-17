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

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()