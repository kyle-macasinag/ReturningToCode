#   The Pay Calculator Script Below Imports The Previous Pay Calculator, Then Adds Overtime If Applicable.


import pay_calculator


def new_calculator():

    pay_calculator.calculate_pay()

    if pay_calculator.hours_worked > 40:

        pay_calculator.total_pay

        new_pay_rate = pay_calculator.pay_rate * 1.5

        new_pay_calculation = new_pay_rate * (pay_calculator.hours_worked - 40) + (pay_calculator.total_pay)

        print(f"The Total Pay Will Be {new_pay_calculation}, Including Overtime.")

    elif pay_calculator.hours_worked <= 40:
        pay_calculator.calculate_pay()
new_calculator()