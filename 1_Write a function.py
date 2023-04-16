# TODO: Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# A leap year is divisible by 400 or idivisible by 4 but not by 100
def is_leap(year):
    leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            leap = True
    else:
        leap = False
    return leap

year = int(input('Enter a year: '))
print(is_leap(year))