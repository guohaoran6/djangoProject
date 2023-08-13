# Django Project for Searching the Reading Values and Dates
### project created by HAORAN GUO

## Introduction
This Django project is designed to store and extract relevant data from D0010 files for meter-points in a local database.
It provides a user interface by Django's admin site, allowing users to search for reading values and dates associated 
with either an MPAN or a meter serial number. Additionally, the application displays the filename of the flow file from 
which the reading originated.

## Features
* Store and extract data from D0010 files for meter-points.
* Search for reading values and dates by MPAN or meter serial number.
* Display the filename of the flow file associated with each reading.
* User interface powered by Django's admin site.

## Requirements
* Operating System: macOS or Linux
* Python: Version 3.10 or above
* Django: Version 4.2.0 or above
* Database: SQLite

## Instructions
### Environment Setup 
1. Ensure Python 3.10 or above is installed on your macOS or Linux machine. 
(Refer to [here](https://www.tutorialspoint.com/python/python_environment.htm) if you need info to install the Python compiler)
2. Install the Django library. Execute the following command in the command line: 
```
pip install django
```

Additionally, you can also use a virtual environment if you want:
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### Project Initialization
During project initialization, data migration and table creation operations need to be performed.
1. Run the data migration command: 
```
python manage.py makemigrations
```
2. Run the table creation command: 
```
python manage.py migrate
```

### Database Initialization
In this step, data files are saved to the database.
Execute the following command in the project's root directory:
```
python manage.py mycommand 'path1' 'path2' ...
```
Note: Each file is loaded only once. If duplicate files are encountered, they will be filtered.

### Project Startup
To start the project, run the following command:
```
python manage.py runserver
```
Then, access the application in your web browser at 
```
http://localhost:8000/
```

## Testing
You can find the test report file named as ```Django-project-test-report.pdf``` on the project root directory.
It provides test instructions and test suites with test cases on how to run the tests.

## Maintenance and Expansion
### Project Maintenance
The main focus of maintenance is to add or remove interfaces. Add or remove interfaces in the urls file and implement 
the interface functionality in the views.

### Expansion Points
* Query optimization: 
For handling large amounts of data, prioritize query optimization through index-based data retrieval. If indexing does 
not improve performance, investigate potential issues causing index inefficiency and resolve them to improve query speed.

* Table partitioning: 
If the above optimizations do not suffice, consider partitioning tables. Splitting a table containing large amounts of 
data into multiple tables and performing multi-table queries can help retrieve the required data efficiently.

### Future Work
* UI/UX optimization to make it more user-friendly.
* Allow flow files to be uploaded via the web go through with RESTful API interface.
* Implement a front-end and back-end separation to reduce development and deployment costs and increase collaboration efficiency.
* Add unit tests to enhance system stability and robustness.
