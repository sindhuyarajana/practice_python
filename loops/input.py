# number = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{number} x {i} = {number * i}")

# number = int(input("enter a number: "))
# for i in range(1,number + 1):
#     print(i)

# total = 0
# number = int(input("enter a number: "))
# for i in range(number + 1):
#     total += i

# print(total)
count = 0
number = int(input("enter a number: "))
for i in range(1, number + 1):
    if i % 3 == 0:
        count += 1

print(count)