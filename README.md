# company-hierarchy Rest Api

In this project I created company and team models. and implemented JWT token

Clone Repository using

```bash
git clone https://github.com/jayvpatel112/company-hierarchy.git
```
Docker set up
```bash
docker build .
```
```bash
docker-compose build
```
```bash
docker-compose up
```
All API end points you can check here => http://127.0.0.1:8000/api/

Create Superuser
```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
generate token using Postman or vscode Thunder Client

POST   http://127.0.0.1:8000/api/token/
```bash
{
  "username":"dummy",
  "password":"dummy"
}
```

Create Company

POST   http://127.0.0.1:8000/api/company/

```bash
{
    "name": "dummy",
    "CEO": "dummy",
    "address": "dummy",
    "Inception_date": "1111-11-11"
}
```

company detail

GET   http://127.0.0.1:8000/api/company/uuid/

add your comapny uuid

create team of above company

POST   http://127.0.0.1:8000/api/company/uuid/team/

add your comapny uuid

```bash
{
    "Lead_Name": "Team Lead"
}
```

get team detail

GET   http://127.0.0.1:8000/api/team/

search comapny by name

POST   http://127.0.0.1:8000/api/search/

```bash
{
    "name": "Comapny Name"
}
```
