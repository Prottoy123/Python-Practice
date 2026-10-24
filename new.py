employee_id = int(input("Enter employee ID: "))

total_hours = float(input("Enter total worked hours for the month: "))

hourly_rate = float(input("Enter hourly wage: "))

 

workdays = 5

 

total_hours = (total_hours // 7) * 2

 

worked_hours = max(0, total_hours)

 

salary = worked_hours * hourly_rate

 

print(f"Employee ID: {employee_id}")

print(f"Salary: ${salary:.2f}")