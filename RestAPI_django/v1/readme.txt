Todo List Rest API- Using Django


https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

STEPS Involved
1. Setup django in virtaul environment
2. Install pip install django
3. Start new Project -django-admin startproject 'projectname'
4. Change the working directory to the 'projectname_directory'
5. Run the server once to check if the config is correct-python manage.py runserver
6. (Optional) Create a separate working directory for django project- python manage.py startapp 'projectname'
7. Add the working directory to main directory in INSTALLED_APPS='projectname.apps.ProjectnameConfig'
8. Migrate the database -python manage.py migrate
9. Create Superuser- python manage.py createsuperuser
10.(Optional) verify again if django server is running- python manage.py runserver
11. Create a model in DB that Django ORM will manage -wokingdirectory/models.py #write code there
11.1. Make migrations whenever you make a change - python manage.py makemigrations ,followed by python manage.py migrate
11.2. Register the model with admin in projectname/admin.py 
12. Set the Django Rest Framework- pip install djangorestframework   
12.1. add the rest framework to INSTALLED_APPS 
13. Serialize the model -AKA convert it to JSON format
14. Dispaly the data by modifying views in working directory
15. Last step is to point out URL at the viewset(thats why rest_framwork was not recognized at first)
16. add url files in working directory