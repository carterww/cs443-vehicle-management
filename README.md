# Vehicle Management System

This software system functions as a vehicle management system for a dealership. The system includes a MySQL database to store data, a backend that handles user interaction with the database, and a frontend that allows users to send commands to the backend. The system tracks vehicles, customers, employees, and vehicle sales; this data is presented to the user via a web interface. The backend allows users to create, retrieve, and update records in the database. This system was created primarily in SQL, Python, HTML, CSS, and Javascript with the following libraries/packages/programs: Django, MySQL, Pillow, ChartJS, Sass, and Bootstrap.

## Installation and Configuration

Setting up the project is fairly straightforward and requires a few simple steps.

1. Begin by downloading the project from the Github repository located at https://github.com/carterww/cs443-vehicle-management
2. Create a virtual Python environment for the project. There are several ways to accomplish this, but I personally used venv. The instructions for this can be be found here https://docs.python.org/3/library/venv.html
3. Install the necessary packages in the virtual environment. First you must activate the virtual environment, then run the following commands:
    * pip install Pillow
    * pip install Django
    * pip install mysqlclient
4. Change the DATABASES variable's values to the correct information for your connection and database.
5. Run the following commands:
    * python manage.py makemigrations
    * python manage.py migrate
6. Your database should now contain all the tables for the codebase.

## Known Issues

There is currently as issue that I tested on a different environment where mysqlclient cannot locate the mysql driver for C. From what I've read, Python uses the C driver for connecting and running queries. This issue exists on a Mac environment but not my Windows environment. Currently, I have not found a solution.

## Miscellaneous Information

Each view function is wrapped in a transaction. This is enabled by the ATOMIC_REQUESTS variable located in settings.py under the DATABASES variable. This causes each view function to begin a transaction at the start, and commit at the end of the function. The transaction is rolled back if there are any exceptions produced in the function.

MySQL automatically creates indexes for all primary keys and foreign keys in a table. There is an index added for the vehiclemanagement_sale_date column because this column is typically used in WHERE clauses for analytical data.