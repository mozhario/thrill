#!/bin/bash

echo "Loading users dummy data"
python manage.py loaddata dummy_users
unzip dummy_data/users_dummy.zip -d media_root/