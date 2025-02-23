# Welcome to my database learning tool w/ Docker!

### This is a very introductory application that has a python flask server and PostgreSQL database.

This application has 2 containers that it builds.

One for the Flask server, another for the postgres db.

Docker container usage:
```
Usage:
make run → Builds the Flask and PostgreSQL containers and starts the containers in the background (-d for detached mode).
make logs → Follows the logs for debugging.
make clean → Stops the containers, removes volumes, and clears unused Docker data.
```

Access locally hosted server on:

`http://localhost:5001/`

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

Feel free to create tables and practice sql locally. Don't push anything without my approval.

