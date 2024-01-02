employee_name = input("Enter employee's name: ");
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_pay = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

def calculatePayroll(gross_pay, federal_rate, state_rate, total_deduction, net_pay):
	gross_pay = hourly_pay * hours_worked
	federal_rate= (federal_tax / 100) * gross_pay
	state_rate = (state_tax / 100) * gross_pay
	total_deduction = federal_tax + state_tax
	net_pay = gross_pay - total_deduction
	return gross_pay, federal_rate, state_rate, total_deduction, net_pay

calculatePayroll()
print()
print("Divine Mercy Payroll statement for the month of December")
print("Employee Name: " + employee_name)
print(f"Hours worked: {hours_worked}")
print(f"Pay Rate: ${hourly_pay}")
print(f"Gross pay: ${gross_pay}")

print("Deductions: ")
print(f"Federal Withholding ({federal_tax}%): ${federal_rate}")
print(f"State Withholding ({state_tax}%): ${state_rate}")
print(f"Total Deduction: ${total_deduction}")
print(f"Net pay: ${net_pay}")
