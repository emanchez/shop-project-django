#!/bin/bash
python3 -m pip install -r requirements.txt
# Force migrations to run
python manage.py migrate --no-input
# Collect static files
python manage.py collectstatic --no-input
# Exit build script
exit 0