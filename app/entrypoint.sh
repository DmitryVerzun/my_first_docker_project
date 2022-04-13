#!/bin/sh

echo "I can't believe it! It's really working!"

#sorry for copypaste, i'm bad with bash

echo "Initiating logger"
python start_logger.py
echo "Logger initiated successfully"

if [ "$ENVIRONMENT" = "development" ]
then
    echo "Removing development database and creating a brand new one..."
    python start_database.py
    python create_tables.py
    echo "Database created"
    echo "Seeding database"
    python seed_database.py
    echo "Database filled with sample data"
fi

while true; do
  sleep 1;
  done
  
exec "$@"