def calc_tax(amount: (int, float), tax_rate: float, age: int) -> int:
    """Calculate the amount of income tax based on the amount, tax rate, and age."""

    if not isinstance(amount, (int, float)):
        raise TypeError("The amount value must be int or float type.")
    if amount < 0:
        raise ValueError("The amount value must be non-negative.")

    if not isinstance(tax_rate, float):
        raise TypeError("The tax_rate must be a float.")
    if not 0 < tax_rate < 1:
        raise ValueError("The tax_rate must be between 0 and 1 (exclusive).")

    if not isinstance(age, int):
        raise TypeError("The age value must be an integer.")
    if age <= 0:
        raise ValueError("The age value must be positive.")

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))
