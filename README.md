This application has 2 containers that it builds.

One for the Flask server, another for the postgres db.

To run the containers:

`docker-compose up --build`

Enter postgresql container:

`docker exec -it my_project-db-1 psql -U myuser -d mydatabase`

Or install a postgres application (such as postico 2) and log in with these credentials:
```
environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
```



