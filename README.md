# Moroccan Tax Calculator

This Python script calculates various financial elements related to Moroccan taxes for both individuals and companies. It includes calculations for income tax (IR), social security contributions (CNSS), and corporate taxes (IS), among others.

## Features

- **Income Calculation**: Computes total annual income based on monthly salary.
- **Social Security (CNSS)**: Calculates both employee and employer contributions.
- **Professional Expenses**: Calculates deductible professional expenses.
- **Income Tax (IR)**: Determines the income tax based on the taxable salary.
- **Salary Calculation**: Provides net salary with and without bonuses.
- **Corporate Tax (IS)**: Computes the corporate tax based on company profits.
- **Dividend Tax (ID)**: Calculates the tax on dividends distributed to shareholders.
- **Annual Expenses & Profit**: Summarizes total expenses, profit, and profit after taxes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/moroccan-tax-calculator.git
    cd moroccan-tax-calculator
    ```
2. Ensure you have Python installed. This script requires Python 3.6+.

3. Install any required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   *(Note: If the script uses external libraries, list them in `requirements.txt`.)*

## Usage

### Command Line Interface

Run the script with the following command:
```bash
python main.py
```

You will be prompted to enter the following details:

- **Monthly Income (MAD)**: Your total monthly income.
- **Taxable Salary (MAD)**: The portion of your salary subject to tax.
- **Non-Taxable Bonus (MAD)**: Bonuses that are not subject to tax.
- **Company Monthly Expenses (MAD)**: Regular monthly expenses incurred by the company.
- **Extra Professional Expenses (MAD)**: Additional professional expenses (default is 750 MAD).
- **Extra Company Expenses (MAD)**: Additional company expenses (default is 12,654 MAD).
- **Fiscal Year**: The year for which you are calculating taxes.

### Example

```python
Enter the monthly income (MAD): 20000
Enter the taxable salary (MAD): 5000
Enter the non-taxable bonus (MAD): 3500
Enter the company monthly expenses (MAD): 1000
Enter the extra professional expenses, Def 750 (MAD): 750
Enter the extra company expenses, Def 12654 (MAD): 12654
Enter the fiscal year: 2023
```

### Output

The script will output a detailed summary of the following:

1. **Monthly Salary Details**:
   - CNSS Employee Contribution
   - CNSS Employer Contribution
   - Professional Expenses
   - Income Tax (IR)
   - Salary with and without bonuses

2. **Company Expenses & Management**:
   - Total Income
   - Total Annual Salary
   - Total Annual Expenses
   - Profit before and after taxes

3. **Summary**:
   - Total Taxes
   - Profit After Fiscal Year
   - Real Total Profit

## Customization

You can customize the script to fit specific needs by modifying the parameters or functions in `salary_calculator` and `company_taxes`. The current default values in the script are tailored for the Moroccan tax system.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Moroccan tax rules and regulations were referenced to ensure accuracy. For more detailed information, you can visit [makeitlegal.ma](https://makeitlegal.ma) or consult with a local tax advisor.

---
