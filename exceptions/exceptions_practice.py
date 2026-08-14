# try:
#     print(10 / 0)
# except:
#     print("Something went wrong")
""
#Write a program that asks the user for a number and handles the error if they enter text instead of a number.
# def main():
#     try:
#         x = int(input("Enter a number: "))
#         print(x)
#     except ValueError:
#         print("Please enter a valid number.")

# main()

def main():
    try:
        numbers = [10, 20, 30]
        print(numbers[5])
    except IndexError:
        print("Give a Valid Index")
main()