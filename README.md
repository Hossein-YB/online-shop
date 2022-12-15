
1 first clone project and run
'''docker-compose up --build '''

2 after that run command 
'''docker-compose exec web python manage.py migrate'''

3 after run migrate run command
'''docker-compose exec web python manage.py collectstatic'''

4 and create superuser
'''docker-compose exec web python manage.py createsuperuser'''
