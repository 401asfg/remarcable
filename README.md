# Build instructions
## .env file
In the root of this project, create a .env file with the following example variables:

```
DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=remarcable_db
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=remarcable_password
DATABASE_HOST=db
DATABASE_PORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost
SECRET_KEY=secret
```

## Ports
This project uses port 8000 for the server and port 5432 for the database, make sure both of these are free.

## Docker
Build the project with docker compose. In bash this can be run with the following command:

```
docker compose up --build
```

## Viewing the webpage
Navigate to localhost:8000

# Assumptions
## Initial data
I originally populated the database using the django admin interface, as instructured. However, the data would not be populated when pushed to and cloned from git, since its actual data was only being persisted in a volume at the time.

compose.yaml
```
services:
  ...
  db:
    ...
    volumes:
      - db-data:/var/lib/postgresql
    ...
volumes:
  db-data:
```

My solution to this was create an initial_data.json fixture (created by dumping the data from the Product, Category, and Tag tables into it), a migration to load the data from that file, and to modify compose.yaml to run the migrations when creating the server.

## Project structure

I considered creating a sub directory in remarcable_app called "products". This would house all the views, filters, tables, and urls related to products. There would be a urls file in the root that would redirect to a "/product_list" url (defined in products/urls.py). There would also be a root filters file that would define the SearchFilter class. I also considered creating a "products" sub directory in the templates directory. All of this would keep the common filters, views, and tables seperate from those designed specifically for the products, of making the project navigable should it be extended (say if there became views for the categories, tags, or a new model).

However, I decided not to do this, as it seems overkill for this type of assignment. This is just what I would do if I needed to expand upon this project.

## Model filters
The filter methods filter_category and filter_tags aren't actually required to the filters function since ModelChoiceFilter and ModelMultipleChoiceFilter already implement their functionality by default. I wrote these methods because I was concerned that using these filters might make it seem like I'm trying to get around actually writing querysets, which is being evaluated through this project.
