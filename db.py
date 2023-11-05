import mysql.connector

# Define the MySQL connection parameters
host = 'localhost'  # Replace with your MySQL server's hostname or IP address
user = 'root'  # Replace with your MySQL username
password = 'Believe@raj25'  # Replace with your MySQL password
database = 'my_new_database'  # Replace with your database name

# Connect to the MySQL server and select the database
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Define the CREATE TABLE statement for the "employees" table
    create_table_query = """
    CREATE TABLE employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        city VARCHAR(255),
        role VARCHAR(255)
    )
    """

    # Execute the CREATE TABLE statement
    cursor.execute(create_table_query)

    print("Table 'employees' created successfully.")

    # Sample data for three employees
    employee_data = [
        ('John Doe', 'New York', 'Manager'),
        ('Jane Smith', 'Los Angeles', 'Developer'),
        ('Bob Johnson', 'Chicago', 'Designer')
    ]

    # Define and execute INSERT statements to add sample data
    insert_query = "INSERT INTO employees (name, city, role) VALUES (%s, %s, %s)"

    for employee in employee_data:
        cursor.execute(insert_query, employee)

    # Commit the changes to the database
    connection.commit()

    print("Sample data added to the 'employees' table.")

except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
