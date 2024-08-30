def calculate_tva(total_sales_local, total_sales_international):
    # TVA is paid only on local sales
    tva_rate = 0.20
    tva = total_sales_local * tva_rate
    return tva

def calculate_is(profit, year):
    # IS rates based on profit and year
    is_tax_rates = {
        2022: {
            "low": 0.10,  # 10% for profits less than 300,000 MAD
            "mid": 0.20,  # 20% for profits between 300,001 and 1,000,000 MAD
            "high": 0.31  # 31% for profits more than 1,000,001 MAD
        },
        2023: {
            "low": 0.125,  # 12.5% for profits less than 300,000 MAD
            "mid": 0.20,  # 20% for profits between 300,001 and 1,000,000 MAD
            "high": 0.2875  # 28.75% for profits more than 1,000,001 MAD
        },
        2024: {
            "low": 0.15,  # 15% for profits less than 300,000 MAD
            "mid": 0.20,  # 20% for profits between 300,001 and 1,000,000 MAD
            "high": 0.255  # 25.5% for profits more than 1,000,001 MAD
        },
        2025: {
            "low": 0.175,  # 17.5% for profits less than 300,000 MAD
            "mid": 0.20,  # 20% for profits between 300,001 and 1,000,000 MAD
            "high": 0.2275  # 22.75% for profits more than 1,000,001 MAD
        },
        2026: {
            "low": 0.20,  # 20% for profits less than 300,000 MAD
            "mid": 0.20,  # 20% for profits between 300,001 and 1,000,000 MAD
            "high": 0.20  # 20% for profits more than 1,000,001 MAD
        }
    }
    rates = is_tax_rates.get(year, is_tax_rates[2022])  # Default to 2022 rates if year not found

    if profit <= 300000:
        return profit * rates["low"]
    elif profit <= 1000000:
        return profit * rates["mid"]
    else:
        return profit * rates["high"]

def calculate_id(dividends, year):
    # ID tax rates based on the year
    id_tax_rates = {
        2022: 0.15,
        2023: 0.1375,
        2024: 0.125,
        2025: 0.1125,
        2026: 0.10
    }
    id_tax_rate = id_tax_rates.get(year, 0.15)  # Default to 15% if year not found
    return dividends * id_tax_rate

def main():
    print("Company Taxation Calculator for Morocco\n")
    
    while True:
        try:
            year = int(input("Enter the year (2022-2026): "))
            if year < 2022 or year > 2026:
                raise ValueError("Year out of range. Please enter a year between 2022 and 2026.")
            total_sales_local = float(input("Enter the total local sales (in MAD): "))
            total_sales_international = float(input("Enter the total international sales (in MAD): "))
            total_expenses = float(input("Enter the total expenses (in MAD): "))
            dividends = float(input("Enter the total dividends (in MAD): "))
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter numeric values.")
            continue

        total_sales = total_sales_local + total_sales_international
        profit = total_sales - total_expenses
        
        tva = calculate_tva(total_sales_local, total_sales_international)
        is_tax = calculate_is(profit, year)
        id_tax = calculate_id(dividends, year)
        
        print("\n--- Tax Calculation ---")
        print(f"Year: {year}")
        print(f"Total Sales: {total_sales:.2f} MAD")
        print(f"Total Expenses: {total_expenses:.2f} MAD")
        print(f"Profit: {profit:.2f} MAD")
        print(f"TVA (Tax on Value Added): {tva:.2f} MAD")
        print(f"IS (Corporate Tax): {is_tax:.2f} MAD")
        print(f"ID (Dividends Tax): {id_tax:.2f} MAD")
        print("----------------------\n")
        
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
