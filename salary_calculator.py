def calculate_cnss_employee(salary):
    if salary <= 6000:
        return salary * (2.26/100 + 3.96/100 + 0.52/100)
    else:
        return salary * (2.26/100) + 6000 * (3.96/100 + 0.52/100)

def calculate_cnss_employer(salary):
    if salary <= 6000:
        return salary * (6.40/100 + 1.05/100 + 7.93/100 + 4.11/100 + 1.6/100)
    else:
        return salary * (6.40/100 + 4.11/100 + 1.6/100) + 6000 * (1.05/100 + 7.93/100)

def calculate_total_cnss(salary):
    return calculate_cnss_employee(salary) + calculate_cnss_employer(salary)

def calculate_professional_expenses(salary, max_expenses=2500):
    # max_expenses = 2500
    expenses = salary * 0.2
    return min(expenses, max_expenses)

def calculate_ir(taxable_income):
    if taxable_income <= 2500:
        return 0
    elif taxable_income <= 4166:
        return taxable_income * 0.10 - 250
    elif taxable_income <= 5000:
        return taxable_income * 0.20 - 666.67
    elif taxable_income <= 6666:
        return taxable_income * 0.30 - 1166.67
    elif taxable_income <= 15000:
        return taxable_income * 0.34 - 1433.33
    else:
        return taxable_income * 0.38 - 2033.33

def calculate_final_salary(salary):
    # Step 1: Calculate CNSS
    cnss_employee = calculate_cnss_employee(salary)
    
    # Step 2: Calculate Professional Expenses
    prof_expenses = calculate_professional_expenses(salary)
    
    # Step 3: Calculate Taxable Income for IR
    taxable_income = salary - cnss_employee - prof_expenses
    
    # Step 4: Calculate IR
    ir = calculate_ir(taxable_income)
    
    # Step 5: Calculate Final Salary
    final_salary = salary - cnss_employee - ir
    
    return final_salary, cnss_employee, ir

def main():
    while True:
        try:
            salary = float(input("Enter the gross salary in MAD (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        final_salary, cnss_employee, ir = calculate_final_salary(salary)
        
        print(f"\nSalary: {salary:.2f} MAD")
        print(f"CNSS (Employee): {cnss_employee:.2f} MAD")
        print(f"IR: {ir:.2f} MAD")
        print(f"Final Salary: {final_salary:.2f} MAD")
        print("------------")

if __name__ == "__main__":
    main()

