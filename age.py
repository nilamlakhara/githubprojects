try:
    years = int(input("Enter age in years: "))
    print("Months:", years * 12)
    print("Days:", years * 365)
except:
    print("Invalid input")