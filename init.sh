#!/bin/bash

# Init db schema and initial data 
echo "Setting up database and initial data"
python manage.py migrate
python manage.py loaddata initial_groups_and_permissions

# Create admin user
echo "Create super admin user"
python manage.py createsuperuser 