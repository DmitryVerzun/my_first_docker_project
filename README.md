# My first docker project
This project attempts to implement a PostgreSQL database and interaction with it through SQLAlchemy through Docker. Charachters from Skyrim are used as sample data because of their near-infinite quantity and the ease of finding quotes.

## Status

Fails at the stage of building a container (entrypoint.sh and other scripts not recognized).

Currently supports the following functions (use --help for details on each one):

1. Adding / deleting heroes from the database. Script name - add_hero.py
2. Adding slogan to a  hero. Script name - add_slogan.py
3. Adding a backstory to a hero. Script name - add_backstory.py
4. Creating any number of random confrontations (for details on the power mechanics see function documentation). Script name - add_random_confrontation.py

## Usage
Build the image, start a container and launch it in background (and ready for commands!):
```
docker-compose up --build -d
```
Scrripts that automatically run when container is started (in entrypoint.sh)
```
docker-compose exec app python start_logging.py
docker-compose exec app python start_database.py
docker-compose exec app python seed_database.py
```
Then python commands can be executed with the following command:
```
docker-compose exec app python scriptname
```
Most things are logged, use this command to acess:
```
docker-compose exec app cat log.txt
```
## Bugs
Something wrong with the slogan-hero relationship. Will fix later
## To do
* Add volumes for production
* Refactor app structure (had a problem with imports)
* Configure environments properly
