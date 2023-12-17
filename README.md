# Data-analytics-project

# MySQL Database Connection and Table Creation

This repository contains a Python script that demonstrates how to connect to a MySQL database, create a table, and insert sample data. Below are the details and steps to use the script:

## Prerequisites

Make sure you have the following prerequisites installed:

- Python
- MySQL Server

Install the required Python package using the following command:

```bash

pip install mysql-connector-python


Before running the script, update the MySQL connection parameters in the script:

import mysql.connector

# Define the MySQL connection parameters
host = 'localhost'  # Replace with your MySQL server's hostname or IP address
user = 'root'  # Replace with your MySQL username
password = 'yourpassword'  # Replace with your MySQL password
database = 'my_new_database'  # Replace with your database name

Run the script create_table.py to create the 'employees' table and insert sample data.

python create_table.py


The script (create_table.py) performs the following tasks:

Connects to the MySQL server.
Creates a table named 'employees' with columns: id, name, city, and role.
Inserts sample data for three employees into the 'employees' table.

Connects to the MySQL server.
Creates a table named 'employees' with columns: id, name, city, and role.
Inserts sample data for three employees into the 'employees' table.
