name = str (input ("Enter your name: "))
basic_salary = int(input("Enter your basic salary: "))
allowance = int(input("Enter your allowance: "))
# Gross salary is before tax , which is basic + allowance
gross_salary = basic_salary+allowance
if gross_salary <= 30000:
  tax_rate = 0
elif gross_salary > 30000 and gross_salary <=50000:
  tax_rate = 10
else:
  tax_rate = 15

tax_amount = gross_salary*tax_rate/100

print (tax_amount)
net_salary = gross_salary-tax_amount
print("After tax salary: ",net_salary)