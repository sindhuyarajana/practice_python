def is_leap(year):
    
    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not a Leap year")
    elif year % 4 == 0:
        print("Leap year")
    else:
        print("Not a Leap year")
    
def main():
    year = int(input("Enter a Year: "))
    is_leap(year)

main()