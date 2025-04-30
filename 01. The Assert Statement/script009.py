"""
The calculate_income_tax() function is given (no argument validation).

The function is supposed to work as follows:
- for age 18 or under, returns the minimum of the following two values:
    - amount * tax_rate
    - 5000
- for age over 18 and age less than or equal to 65 returns:
    - amount * tax_rate
- for the age over 65, it returns a minimum of the following two values:
    - amount * tax_rate
    - 8000

There are two bugs in the calculate_income_tax() function implementation.

Try to correct these bugs so that the function passes the tests implemented
in the test_calculate_income_tax() function.

The test_calculate_income_tax() function asserts the following test cases:
    - calculate_income_tax(60000, 0.15, 10) == 5000
    - calculate_income_tax(60000, 0.15, 18) == 5000
    - calculate_income_tax(60000, 0.15, 19) == 9000
    - calculate_income_tax(60000, 0.15, 65) == 9000
    - calculate_income_tax(60000, 0.15, 66) == 8000
"""

def calculate_income_tax(amount: float, tax_rate: float, age: int) -> int:
    """
    Calculates the income tax based on the given amount, tax rate, 
    and age.

    :param amount: The amount of income.
    :param tax_rate: The tax rate as a decimal.
    :param age: The age of the taxpayer.
    :return: The amount of income tax.
    """
    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

def test_calculate_income_tax():
    assert calculate_income_tax(60000, 0.15, 10) == 5000        
    assert calculate_income_tax(60000, 0.15, 18) == 5000
    assert calculate_income_tax(60000, 0.15, 19) == 9000
    assert calculate_income_tax(60000, 0.15, 65) == 9000
    assert calculate_income_tax(60000, 0.15, 66) == 8000

if __name__ == '__main__':
    test_calculate_income_tax()
