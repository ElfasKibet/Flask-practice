# Notebook App

## Models

-   Category (id, name, created_at)
-   Entry (id, note, user_id, category_id, created_at, updated_at, deleted_at)
-   User (id, full_name, email_address, password, created_at, updated_at)
-   Task (id, name, status, user_id, created_at)

-   Maybe cover role based auth

## Database (with sqlalchemy)

-   Install the two packges `pipenv install flask-sqlalchemy flask-migrate`
-   How to get the possible commands `flask db --help`
-   Init migrations with `flask db init` -- run only once
-   Create/autogenerate migration files with `flask db migrate -m ""`
-   Apply our migration with `flask db upgrade`