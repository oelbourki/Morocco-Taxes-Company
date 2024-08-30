from salary_calculator import *
from company_taxes import *

def main(monthly_income, taxable_salary, non_taxable_bonus, company_monthly_expenses, extra_prof_expenses, extra_company_expenses, year):
    # Calculate total annual income
    total_income = monthly_income * 12

    # CNSS calculations
    cnss_employee = calculate_cnss_employee(taxable_salary)
    cnss_employer = calculate_cnss_employer(taxable_salary)
    total_cnss = cnss_employee + cnss_employer

    # Professional expenses calculation
    prof_expenses = calculate_professional_expenses(taxable_salary) + extra_prof_expenses

    # IR base calculation
    ir_base = taxable_salary - cnss_employee - prof_expenses
    ir = calculate_ir(ir_base)

    # Salary calculations
    salary_without_bonus = taxable_salary - ir - cnss_employee
    salary_with_bonus = salary_without_bonus + non_taxable_bonus

    # Total monthly expenses calculation
    total_monthly_expenses = cnss_employee + cnss_employer + ir

    # Annual salary and expenses calculation
    year_salary = (taxable_salary + non_taxable_bonus + company_monthly_expenses) * 12
    total_expenses = year_salary + extra_company_expenses

    # Profit calculation
    profit = total_income - total_expenses

    # IS calculation
    IS = calculate_is(profit, year=year)

    # Dividend calculation
    dividend = profit - IS

    # ID calculation
    ID = calculate_id(dividend, year=year)

    # Other expenses calculation
    other_expenses = company_monthly_expenses * 12

    # Taxes summary calculation
    taxes_summary = ID + IS + total_monthly_expenses * 12

    # Profit after fiscal year calculation
    profit_after_fiscal_year = profit - ID - IS

    # Total profit calculation
    total_profit = profit_after_fiscal_year + salary_with_bonus * 12

    # Real total profit calculation
    real_total_profit = total_profit + total_monthly_expenses * 12

    # Printing results in a structured format
    print("\n=== YOUR INPUTS ===")
    print(f"Monthly Income: {monthly_income} MAD")
    print(f"Taxable Salary: {taxable_salary} MAD")
    print(f"Non-Taxable Bonus: {non_taxable_bonus} MAD")
    print(f"Company Monthly Expenses: {company_monthly_expenses} MAD")
    print(f"Extra Professional Expenses: {extra_prof_expenses} MAD")
    print(f"Extra Company Expenses: {extra_company_expenses} MAD")
    print(f"Year of Calculation: {year}\n")

    print("=== YOUR MONTHLY SALARY ===")
    print(f"CNSS Employee Contribution: {cnss_employee:.2f} MAD")
    print(f"CNSS Employer Contribution: {cnss_employer:.2f} MAD")
    print(f"Total CNSS Contribution: {total_cnss:.2f} MAD")
    print(f"Professional Expenses: {prof_expenses:.2f} MAD")
    print(f"IR Base: {ir_base:.2f} MAD")
    print(f"IR: {ir:.2f} MAD")
    print(f"Salary without Bonus: {salary_without_bonus:.2f} MAD")
    print(f"Salary with Bonus: {salary_with_bonus:.2f} MAD")
    print(f"Total Monthly Expenses (CNSS/IR): {total_monthly_expenses:.2f} MAD\n")

    print("=== YOUR COMPANY EXPENSES/MANAGEMENT ===")
    print(f"Total Income: {total_income:.2f} MAD")
    print(f"Total Annual Salary: {year_salary:.2f} MAD")
    print(f"Total Annual Expenses: {total_expenses:.2f} MAD")
    print(f"Profit: {profit:.2f} MAD")
    print(f"IS for Year {year}: {IS:.2f} MAD")
    print(f"ID for Year {year}: {ID:.2f} MAD")
    print(f"Other Annual Expenses: {other_expenses:.2f} MAD\n")

    print("=== SUMMARY ===")
    print(f"Total Taxes Summary: {taxes_summary:.2f} MAD")
    print(f"Profit After Fiscal Year: {profit_after_fiscal_year:.2f} MAD")
    print(f"Total Profit: {total_profit:.2f} MAD")
    print(f"Real Total Profit: {real_total_profit:.2f} MAD")

def get_input(prompt, default):
    user_input = input(prompt)
    if user_input == "":
        return default
    else:
        return float(user_input) if isinstance(default, float) else int(user_input)
    
if __name__ == "__main__":
    # Interactive input for arguments
    # monthly_income = float(input("Enter the monthly income (MAD): "))
    # taxable_salary = float(input("Enter the taxable salary (MAD): "))
    # non_taxable_bonus = float(input("Enter the non-taxable bonus (MAD): "))
    # company_monthly_expenses = float(input("Enter the company monthly expenses (MAD): "))
    # extra_prof_expenses = float(input("Enter the extra professional expenses, Def 750 (MAD): "))
    # extra_company_expenses = float(input("Enter the extra company expenses, Def 12654 (MAD): "))
    # year = int(input("Enter the fiscal year: "))
    monthly_income = get_input("Enter the monthly income (MAD): ", 20000)
    taxable_salary = get_input("Enter the taxable salary (MAD): ", 5000)
    non_taxable_bonus = get_input("Enter the non-taxable bonus (MAD): ", 3500)
    company_monthly_expenses = get_input("Enter the company monthly expenses (MAD): ", 1000)
    extra_prof_expenses = get_input("Enter the extra professional expenses, Def 750 (MAD): ", 750)
    extra_company_expenses = get_input("Enter the extra company expenses, Def 12654 (MAD): ", 12654)
    year = get_input("Enter the fiscal year: ", 2023)

    # Call the main function with user inputs
    main(monthly_income, taxable_salary, non_taxable_bonus, company_monthly_expenses, extra_prof_expenses, extra_company_expenses, year)
