# try:
#     print(10 / 0)
# except:
#     print("Something went wrong")
""
def main():
    try:
        x = int(input("Enter a number: "))
        print(x)
    except ValueError:
        print("Please enter a valid number.")

main()