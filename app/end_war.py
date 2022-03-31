#WARNING! This script WILL wipe out most of the database and has to be turned of by CTRL + C (will fix later)
#When performed on the seed database, will always lead to Thalmor victory
#That's because one of their heroes is invincible for the purpose of debugging

from data_interaction import *

def main():
    while True:
        add_random_confrontation()