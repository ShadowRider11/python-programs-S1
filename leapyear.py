start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

if end_year < start_year:
    print("Ending year must be greater than or equal to the starting year.")
else:
    print("Leap years from", start_year, "to", end_year, ":")
    year = start_year
    while year <= end_year:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
        year += 1
