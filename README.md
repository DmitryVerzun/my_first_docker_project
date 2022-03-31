# My first docker project
This project attempts to implement a PostgreSQL database and interaction with it through SQLAlchemy through Docker. Charachters from Skyrim are used as sample data because of their near-infinite quantity and the ease of finding quotes.

## Status

Fails at the stage of building a container (entrypoint.sh and other scripts not recognized).

The SQLAlchemy part is fully functional but only if you run it with a jupyter notebook. It currently supports the following functions (use --help for details on each one):

1. Adding / deleting heroes from the database. Script name - add_hero.py
2. Adding slogan to a  hero. Script name - add_slogan.py
3. Adding a backstory to a hero. Script name - add_backstory.py
4. Creating a random confrontation (for details on the power mechanics see function documentation). Script name - add_random_confrontation.py
5. Ending the war with end_war.py This is achieved by running the add_random_confrontation() function in an infinite loop until only one side is left. WARNING: running this WILL wipe out most of the database.

## Usage
Build the image, start a container and launch it in background (and ready for commands!):
```
docker-compose up --build -d
```
Scrripts for initializing and seeding database (will automate later, see Bugs section)
```
docker-compose exec app python start_logging.py
docker-compose exec app python start_database.py
docker-compose exec app python seed_database.py
```
Then python commands can be executed with the following command:
```
docker exec python_cont python scriptname
```
Most things are logged, use this command to acess:
```
docker-compose exec app cat log.txt
```
## Bugs
The python container will exit with code 0 if all entrypoint.sh execution is commented. If it is not, the execution will fail with the following message:
>ERROR: for python  Cannot start service app: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "usr/src/app/entrypoint.sh": stat usr/src/app/entrypoint.sh: no such file or directory: unknown

Something wrong with the slogan-hero relationship. Will fix later
## To do
* Add volumes for production
* Refactor app structure (had a problem with imports)
* Configure environments properly