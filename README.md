This application has 2 containers that it builds.

One for the Flask server, another for the postgres db.

Docker contianer usage:
```
Usage:
make build → Builds the Flask and PostgreSQL containers.
make up → Starts the containers in the background (-d for detached mode).
make down → Stops and removes the containers.
make logs → Follows the logs for debugging.
make clean → Stops the containers, removes volumes, and clears unused Docker data.
```

Enter postgresql container through terminal:

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



