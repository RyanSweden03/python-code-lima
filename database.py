import mysql.connector
from config import DATABASE_CONFIG
from faker import Faker

faker = Faker()

def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

def create_employee_table():
    """
    Creates the 'employees' table if it does not exist already.
    The table has columns: id, name, age, city, salary.
    """
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                city VARCHAR(100),
                salary DECIMAL(10, 2)
            );
        ''')
        connection.commit()
        print("Table 'employees' created or verified successfully.")

    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")


def generate_fake_employee_data(record_count=5):
    """
    Generates fake employee data using the Faker library.
    
    Args:
        record_count (int): The number of fake records to generate.
    
    Returns:
        list: A list of tuples containing fake employee data.
    """
    data = []
    for _ in range(record_count):
        name = faker.name()
        age = faker.random_int(min=18, max=65)
        city = faker.city()
        salary = round(faker.random_number(digits=4, fix_len=True), 2) 
        data.append((name, age, city, salary))
    return data

def insert_fake_data(record_count=2):
    try:
        data = generate_fake_employee_data(record_count)
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.executemany(
            "INSERT INTO employees (name, age, city, salary) VALUES (%s, %s, %s, %s)",
            data
        )
        connection.commit()
        print(f"{record_count} records successfully inserted.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()  
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        connection.rollback()  
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")


def get_all_employees():
    
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees;")
        rows = cursor.fetchall()
        return rows

    except mysql.connector.Error as err:
        print(f"Error fetching data from MySQL: {err}")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Database connection closed.")

