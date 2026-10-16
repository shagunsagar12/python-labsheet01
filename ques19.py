p = int(input("Enter loan amount = "))
r = int(input("Enter rate = "))
n = int(input("Enter months = "))

monthly_rate = r / (12 * 100)

emi = (p * monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)

print("Monthly EMI =", emi)