while True:
    year = int(input("Enter a year (0 to exit): "))

    if year == 0:
        print("End")
        break

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")