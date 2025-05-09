import unittest


class PaymentGateway:
    def process_payment(self, amount):
        # Code to process payment
        return True


def is_production_environment():
    # Code to check if it is a production environment
    return True


class TestPaymentGateway(unittest.TestCase):
    @unittest.skipIf(not is_production_environment(), "Not in production environment")
    def test_process_payment(self):
        amount = 1000
        gateway = PaymentGateway()
        self.assertTrue(gateway.process_payment(amount))


if __name__ == "__main__":
    unittest.main()
