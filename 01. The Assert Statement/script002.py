"""
Assert the is_canada variable using the assert statement:

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_canada = 'CAN' in countries

Expected action: Raising AssertionError.
"""

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_canada = 'CAN' in countries

assert is_canada, "Canada not found in the countries list."
