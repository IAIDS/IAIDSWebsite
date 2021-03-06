#! /bin/bash
#find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find . -path "*/migrations/*.pyc"  -delete

# global variables
database="IAIDSWebsite"

mysql -u vagrant -pProject1! -D IAIDSWebsite -e "DROP DATABASE IAIDSWebsite;"
mysql -u vagrant -pProject1! -e "CREATE DATABASE IAIDSWebsite;"
echo "Dropped Database and created" $database

python3 /home/vagrant/IAIDSWebsite/IAIDSWebsite/manage.py makemigrations
python3 /home/vagrant/IAIDSWebsite/IAIDSWebsite/manage.py migrate
echo "Set up your new super user:"
python3 /home/vagrant/IAIDSWebsite/IAIDSWebsite/manage.py createsuperuser
