import unittest
import sqlite3
from customers import CustomersDB


class TestCustomersDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(":memory:")
        cls.cursor = cls.connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cls.cursor.execute(create_table_sql)

        customers_data = [
            ("John", "Smith", "john.smith@mail.com", "111", "USA"),
            ("John", "Doe", "john.doe@mail.com", "333", "USA"),
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cls.cursor.executemany(insert_sql, customers_data)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_add_customer(self):
        db = CustomersDB(self.connection)
        db.add_customer("Mike", "Doe", "mike.doe@mail.com", "222", "USA")

        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM customers
            ORDER BY first_name, last_name;
            """
        )

        expected = [
            ("John", "Doe", "john.doe@mail.com", "333", "USA"),
            ("John", "Smith", "john.smith@mail.com", "111", "USA"),
            ("Mike", "Doe", "mike.doe@mail.com", "222", "USA"),
        ]
        actual = cursor.fetchall()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
