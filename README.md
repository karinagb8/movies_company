# movies_company

Consultas a la api:
http://127.0.0.1:8000/movies_company/api/movies_api/persons/
http://127.0.0.1:8000/movies_company/api/movies_api/movies/

Create Aliases
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey user:key" -X POST --data '{"name":"alias"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'