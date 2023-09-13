# django-learning-platform
First Clone Project
-     git clone https://github.com/Ali-Ahmadii/django-learning-platform.git
For Activating Virtual Enviroment In Windows Write This Command In Project Folder
-      ./venv/Scripts/activate
Also If You Want Install Whole Packages Together With requirements.txt File You Can Write This Command In Command Line Or In Your Terminal
-     pip install -r requirements.txt
You Can Make Sure About Installed Python Packages By This Command
-     pip freeze
Then We Will Sync Our Database Using These Commnads(we use default sqllite engine here for simplicity)
-       python manage.py makemigrations
-       python manage.py migrate
Running On localhost
-       python manage.py runserver