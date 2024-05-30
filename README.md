# Django File Upload Application

This is a Django-based web application that allows users to upload Excel or CSV files and view the uploaded data. This project demonstrates Django development skills, including form handling, file uploads, template rendering, and basic deployment.

## Features

- File Upload Form**: A web page with a form allowing users to upload Excel or CSV files.
- Data Handling**: Uploaded files are processed using the `pandas` library, and the data is displayed in a tabular format on the success page.
- Static Files**: Custom CSS is used to style the form and success pages.
- Deployment**: The project can be deployed to an open-source server like Heroku.

## Project Structure

myproject/
├── myapp/
│ ├── templates/
│ │ ├── upload.html
│ │ ├── upload_success.html
│ ├── forms.py
│ ├── views.py
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── migrations/
├── static/
│ ├── styles.css
├── myproject/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── manage.py
├── requirements.txt

### Prerequisites

- Python 3.x
- Django
- Pandas
- Openpyxl

### Usage
Upload a file: Go to the upload page, choose an Excel or CSV file, and click "Upload".
View data: After uploading, the data will be displayed in a tabular format on the success page.

### Acknowledgments
Django Documentation
Pandas Documentation
