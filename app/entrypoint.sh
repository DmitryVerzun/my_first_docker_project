#!usr/bin/bash

echo "I can't believe it! It's really working!"

#sorry for copypaste, i'm bad with bash
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Initiating logger"
python logger.py
echo "Logger initiated successfully"

if [ "$ENVIRONMENT" = "development" ]
then
    echo "Removing development database and creating a brand new one..."
    python start_database.py
    echo "Database created"
    echo "Seeding database"
    python seed_database.py
    echo "Database filled with sample data"
fi

exec "$@"
