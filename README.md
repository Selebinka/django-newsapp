# News App

API for viewing, adding to favorites and deleting news from the portal https://newsapi.org/

# Requirements
    *  Python==3.8
    *  Django/DRF
    *  Celery
    *  OAuth2
    *  PostgreSQL

You can see all dependencies in the "requirements.txt" file.  
Use *pip install -r requirements.txt* to install

# Make migrations

*python manage.py makemigrations*  \
*python manage.py migrate*

# Create superUser

*python manage.py createsuperuser*

# Config OAuth2

Add your NEWS_API_KEY to settings.py. \
In http://127.0.0.1:8000/admin/oauth2_provider/application/ create new app. \
Set your application name in *settings.py* OAUTH_APP_NAME.

# Run server commands

*python manage.py runserver* \
*redis-server* \

run the following commands (one in each window):

*celery -A newsapp worker -l info* \
*celery -A newsapp beat -l info*

# API documentation
*http://127.0.0.1:8000/redoc/* \
*http://127.0.0.1:8000/swagger/*
