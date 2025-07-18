class CustomersDB:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add_customer(self, first_name, last_name, email, phone, country):
        sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        self.cursor.execute(sql, (first_name, last_name, email, phone, country))
        self.connection.commit()
        return self.cursor.lastrowid

    def find_customers_by_first_name(self, first_name):
        sql = """
            SELECT *
            FROM customers
            WHERE first_name LIKE ?
            ORDER BY first_name, last_name;"""
        self.cursor.execute(sql, (first_name,))
        return self.cursor.fetchall()

    def find_customers_by_country(self, country):
        sql = """
            SELECT *
            FROM customers
            WHERE country LIKE ?
            ORDER BY first_name, last_name;"""
        self.cursor.execute(sql, (country,))
        return self.cursor.fetchall()
