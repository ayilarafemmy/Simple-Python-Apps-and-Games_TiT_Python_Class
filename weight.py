weight = int(input("What is your weight? "))
unit = input("(K)g or (L)bs: ")
# real value is 2.24
if unit.upper() == "K":
    converted = weight * 2.20462
    print("weight in Lbs:", converted)
elif unit.upper() == "L":
    converted = weight / 2.20462
    print("weight in Kgs:", converted)
else:
    print("Invalid unit. Please try again.")