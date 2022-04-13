#script for filling daatbase with sample data
#DON'T call at production stage

from create_tables import *
from data_interaction import *
from start_database import *


def main():

    #adding Empire heros
    add_hero(side="Empire", name="Hadvar", \
        birthday="0175-11-23", race="Nord", power=6)
    add_hero(side="Empire", name="General Thulius", \
        birthday="0145-06-07", race="Imperial", power=9)
    add_hero(side="Empire", name="Elisif", \
        birthday="0170-02-15", race="Nord", power=4)
    add_hero(side="Empire", name="Rikke", \
        birthday="0165-08-15", race="Nord", power=7)

    #adding Stormcloak heros
    add_hero(side="Stormcloaks", name="Ralof", \
        birthday="0176-09-17", race="Nord", power=6)
    add_hero(side="Stormcloaks", name="Ulfric Stormcloak", \
        birthday="0149-06-07", race="Nord", power=15)
    add_hero(side="Stormcloaks", name="Roggvir", \
        birthday="0170-02-25", race="Nord", power=4)
 
    #adding Thalmor heros
    add_hero(side="Thalmor", name="Nazeem",  \
        birthday="0160-05-01", race="Redguard", power=1)
    add_hero(side="Thalmor", name="Elenwen", \
        birthday="0089-12-04", race="High elf", power=6)
    add_hero(side="Thalmor", name="Ancano", \
        birthday="0050-06-29", race="High elf", power=30)

    #adding_slogans (testing many-to-one relationship)
    add_slogan("Have you always been that ugly?", "Ralof")
    add_slogan("I think I killed more Imperials than you. I was counting!", "Ralof")
    add_slogan("As fearless in death as he was in life.", "Ralof")

    add_slogan("There was no murder! Ulfric challenged Torygg. \
    He beat the High King in fair combat.", "Roggvir")
    add_slogan("Do you know the way? I'm weary and lost.", "Ulfric Stormcloak")

    add_slogan("I want every arrow in the sky!", "General Thulius")
    add_slogan("Ulfric is a fool and a coward", "Elisif")
    add_slogan("Dragonborn huh? Was it your ma or your pa that was the dragon?", "Hadvar")
    add_slogan("The sooner we end this rebellion, the sooner I'll be able to sleep at night.", "Rikke")

    add_slogan("Oh, it took years, but I earned my way to the top.", "Nazeem")
    add_slogan("I actually advise the Jarl on political matters.", "Nazeem")
    add_slogan("I had hoped your scholars would be on a level comparable with my own colleagues.", "Ancano")
    add_slogan("Are you here because you believe you can change the world?", "Ancano")
    add_slogan("You've come for me, have you? You think I don't know what you're up to?", "Ancano")
    add_slogan("Talos was a heroic man, but not a god.", "Elenwen")


if __name__ == "__main__":
    main()