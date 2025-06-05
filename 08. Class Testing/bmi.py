class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height**2)

    def is_healthy(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            return "healthy"
        elif bmi >= 25 and bmi <= 29.9:
            return "overweight"
        else:
            return "obese"
