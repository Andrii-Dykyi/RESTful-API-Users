## RESTful API Project + Socket.IO

### RUN locally:
```sh
$ docker-compose build
$ docker-compose up -d
```
### During the first run don't forget to migrate:
```sh
$ docker-compose run app bash -c "python3 manage.py migrate"
```
### STOP and remove containers:
```sh
$ docker-compose down
```
### HINT: No volumes created for this project that why all data created in container(including DB) will be deleted after containers remove.

### RESTful API:
#### http://127.0.0.1:8000/api/v1
1. ​/users POST
2. /login POST
3. /users/:id GET 
4. ​/users/:id PUT

### FrontEnd:
#### http://127.0.0.1:8080