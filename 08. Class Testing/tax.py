class SimpleTaxCalculator:
    def __init__(self, first_thresh=17.0, second_thresh=32.0, vat_tax_rate=23.0, capital_gains_tax_rate=19.0):
        self.first_thresh = first_thresh / 100.0
        self.second_thresh = second_thresh / 100.0
        self.threshold = 85528
        self.vat_tax_rate = vat_tax_rate / 100.0
        self.capital_gains_tax_rate = capital_gains_tax_rate / 100.0

    def income_tax(self, income):
        if income < self.threshold:
            return income * self.first_thresh
        else:
            return self.threshold * self.first_thresh + (income - self.threshold) * self.second_thresh

    def vat_tax(self, net_price):
        return net_price * self.vat_tax_rate

    def capital_gains_tax(self, profit):
        if profit > 0:
            return profit * self.capital_gains_tax_rate
        return 0
