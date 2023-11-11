print("welcome to yusuf and sons")

initial_principal = float(input("Enter your initial amount: "))
interest_rate = float(input("Enter your interest rate"))
time = float(input("Enter the number of times the interest applied per time period"))
n = float(input("enter the number of time periods elapsed"))

simple_interest = initial_principal * (1 + (interest_rate * time))
compound_interest = initial_principal * (1 + (interest_rate/n))**n*time

print("simple interest = " + str(simple_interest))
print("compound interest = " + str(compound_interest))
