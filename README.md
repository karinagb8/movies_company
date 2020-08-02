# movies_company

Consultas a la api:
http://127.0.0.1:8000/movies_company/api/movies_api/persons/
http://127.0.0.1:8000/movies_company/api/movies_api/movies/

Get Aliasses
curl --dump-header - -H "Content-Type: application/json" -X GET 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'

Create Aliases
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X POST --data '{"name":"{{alias}}"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'

Updating An Existing Resource of Alias
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X PUT --data '{"name":"{{new_alias}}"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/{{id_alias}}/'

Partially Updating An Existing Resource of Alias
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X PATCH --data '{"name":"{{new_alias}}"}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/{{id_alias}}/'

Replace the entire collection of Aliases
curl --dump-header - -H "Content-Type: application/json" -H "AUTHORIZATION: ApiKey {{user}}:{{key}}" -X PUT --data '{"objects": [{"name":"{{alias}}", "id":"{{id}}"}, {"name":"{{alias}}", "id":"{{id}}"}]}' 'http://127.0.0.1:8000/movies_company/api/movies_api/aliases/'


Asumo que hay alias que se repiten entre distintas personas