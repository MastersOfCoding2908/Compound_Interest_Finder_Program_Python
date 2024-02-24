# Let'S See How To Upload Project On Git In PyCharm.
# I am Master'S Of Coding @mastersofcoding2908
print('''
Welcome !
    This Is Compound Interest Finder :\n''')
print("* Values Should Only Be In The Form Of Integers or Decimals *\n")
Principal = float(input("Enter The Principal Amount (In Rupees) : Rs.  "))
Rate = float(input("What Is The Rate Of Interest ? : "))
Time = float(input("What is The Time (In Years) : "))

Compound_hy_year = input('''
Interest is Compounded Annually or Half Yearly,
For Half Yearly Write 'h' or 'H' and For Annually Write 'a' or 'A' : ''')
Compound_hy_year = Compound_hy_year.lower()
if Compound_hy_year == 'h':
     CI = Principal*((1+(Rate/200))^Time*2)
     print("So, Compound Interest(CI) = ", "Rs.", CI - Principal)
     print("And Amount = ", "Rs.", CI)
elif Compound_hy_year == 'a':
  CI = Principal*(1+(Rate/100))
  print("So, Compound Interest(CI) = ","Rs.",CI-Principal)
  print("And Amount = ","Rs.", CI)
else:
    print("You Have Entered A InValid Value. Please Try Again Running This Program!",
          "Thank You!")