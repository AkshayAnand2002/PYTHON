weight=float(input("Please enter the weight: "))
unit= input("Enter unit in Lbs (L) or Kgs (K): ")
if unit.upper()=='L':
    convert= weight*0.45
    print(f"You are {convert} kilos")
else:
    convert=weight/0.45
    print(f"You are {convert} pounds")
