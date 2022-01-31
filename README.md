# MonitorTrafficBack
Web Traffic Monitor

> Basic traffic monitor, the traffic monitor will display details about visitors on the website using IPStack API .


- IPStack 
offers a powerful, real-time IP to geolocation API capable of looking up accurate location data and 
assessing security threats originating from risky IP addresses. 
Results are delivered within milliseconds in JSON or XML format. 
Using the ipstack API you will be able to locate website visitors at first glance and 
adjust your user experience and application accordingly.

## Requirements
* Python 3+;
* PostgreSQL 11+;
* Redis;
* Celery
* PIP modules (см. requirements.txt).

## Configuration file
When deploying, copy the file`configs.json.example` in file `configs.json` in directory 
`monitor/monitor/settings/`.

Example `configs.json` file `monitor/monitor/settings/configs.json.example`.

## Start

1. Create and Activate Virtual environment:

    `python -m venv venv`


2. Install dependencies:

    `pip install -r requirements.txt`


3. Run migrations :

    `python manage.py migrate`


4. Create statics files: 

    `python manage.py collectstatic`


5. Create superuser:

    `python manage.py createsuperuser`


6. Run server:

    `$ python manage.py runserver`


7. Run celery and beat:

    `$ celery -A monitor worker --beat --scheduler django --loglevel=info`
