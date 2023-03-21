# CSVAPI
Django CSV API to upload CSV,insert rows into table and Sort the data and return top 50 employees.
CSV file is provided in the project folder
You have the run below comands:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver
Then open Postman and call http://127.0.0.1:8000/upload-csv/ with GET Method.
Then call http://localhost:8000/top-50-rows/?column_name=emp_name&sort_order=desc&count=50 with POST Method
You can change the coulmn_name(emp_num or emp_name), sort_order(asc,desc), count accordingly.
And you will get the sorted order data for provided number of count or default 50 counts in JSION format.
