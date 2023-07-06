Name=input("please enter your name").strip()
Age=input("please enter your Age").strip()
unit=input("please choose the format:{Months,Weeks,Days, Hours,Minutes,All}").strip()
Months=int(Age)*12
Weeks=Months*8
Days=int(Age)*365
Hours=int(Age)*365*24
Minutes=int(Age)*365*24*60
if unit=="Months":
   print(f"you lived for {Months} months.")
elif unit=="Weeks":
   print(f"you lived for {Weeks} Weeks.")
elif unit=="Days":
   print(f"you lived for {Days} Days.")
elif unit=="Hours":
    print(f"you lived for {Hours} HRS.")
elif unit=="Minutes":
    print(f"you lived for {Minutes} Minutes.")
elif unit=="All":
    print(f"you lived for {Months} months,{Weeks} Weeks, {Days} Days,{Hours} HRS,{Minutes} Minutes.")
else:
    print('Invalid Input')

