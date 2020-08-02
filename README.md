# movies_company

Used Libraries/Frameworks:
=======================================
- Python 3.7.5
- Django 3.0.8
- Tastypie 0.14.3
- sqlite3

How to start:
=======================================
STEP 1: Create a virtualenv with python3:
virtualenv venv --python=python3
STEP 2: Activate the virtualenv:
source venv/bin/activate
STEP 3: Install the packages from py-requirements:
pip install -r py-requirements
STEP 4: Initialize the database:
python manage.py migrate
STEP 5: Access the web site
http://127.0.0.1:8000/admin

Decissions:
=======================================
- The same alias can be used for two or more different users
- Records can only be deleted using the admin site (superusers with is_staff = True)
- The "trusted users" are the ones who are superusers (not staff) and they need an API Key that can be created only by admin users
- I used sqlite because it was easier to start a database. It's not necessary to install any package or create the database, Django manages automaticaly everything. I usually use PostgreSQL.
- All the fields are required
- The fields for 'casting', 'producers' and 'directors' are at Movie's model as a ManyToManyField with a related_name to access from Person's model as 'movies_as_actor_actress', 'movies_as_producer', 'movies_as_director' respectively.

Available URLS:
=======================================
Since this application uses Tastypie, several URLs have different behaviour deppending on the parameters. The GET methods are accesible by everyone. UPDATE and CREATE methods require authentication (API Key) and authorization (is superuser).
The admin site is accesible only by superusers with is_staff = True.

Admin site:
---------------------------------------
http://127.0.0.1:8000/admin


Persons:
---------------------------------------
- GET all the persons: 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/
- UPDATE all the persons (requires data from model Person): 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/
- CREATE one person (requires data from model Person): 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/
- GET the person with id {{id_person}}: 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/{{id_person}}/
- UPDATE the person with id {{id_person}} (requires data from model Person): 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/{{id_person}}/
- GET the resource’s schema for persons: 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/schema/
- GET a subset of items with ids {{id_person1}}, {{id_person2}}: 
http://127.0.0.1:8000/movies_company/api/movies_api/persons/set/{{id_person1}};{{id_person2}}/


Movies:
---------------------------------------
- GET all the movies: 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/
- UPDATE all the movies (requires data from model Movie): 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/
- CREATE one movie (requires data from model Movie): 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/
- GET the movie with id {{id_movie}}: 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/{{id_movie}}/
- UPDATE the movie with id {{id_movie}} (requires data from model Movie): 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/{{id_movie}}/
- GET the resource’s schema for movies: 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/schema/
- GET a subset of items: 
http://127.0.0.1:8000/movies_company/api/movies_api/movies/set/{{id_movie1}};{{id_movie2}};..../


Aliases:
---------------------------------------
- GET all the aliases: 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/
- UPDATE all the aliases (requires data from model Alias): 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/
- CREATE one alias (requires data from model Alias): 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/
- GET the alias with id {{id_alias}}: 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/{{id_alias}}/
- UPDATE the alias with id {{id_alias}} (requires data from model Alias): 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/{{id_alias}}/
- GET the resource’s schema for aliases: 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/schema/
- GET a subset of items: 
http://127.0.0.1:8000/movies_company/api/movies_api/aliases/set/{{id_alias1}};{{id_alias2}};..../


Usage with curl for each URL and request method (action) for aliases:
---------------------------------------
- Get Aliasses
curl --dump-header - -H "Content-Type: application/json" -X GET 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'

- Create Aliases
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X POST --data '{"name":"{{alias}}"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'

- Updating An Existing Resource of Alias
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X PUT --data '{"name":"{{new_alias}}"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/{{id_alias}}/'

- Partially Updating An Existing Resource of Alias
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X PATCH --data '{"name":"{{new_alias}}"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/{{id_alias}}/'

- Replace the entire collection of Aliases
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X PUT --data '{"objects": [{"name":"{{alias}}", "id":"{{id}}"}, {"name":"{{alias}}", "id":"{{id}}"}]}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'


Available methods:
=======================================
- int_to_roman (from utils.py): it converts an integer number to roman numerals
