import datetime

from start_database import *
from start_logging import logging
import random


def randomize_attack_success(power_attacker, power_defender, stealth_factor=2):
    """
    Find if the attacking hero won the fight. Each fight is an unfair coin flip. 
    The probability of winning is calculated in such a way that a 0 
    power difference means 50% victory chance and a 10 power difference means 100% chance.
    Stealth factor is added to attacker's power, default value is 2.
    The probability variable is not a probability in a mathematical sense and can be < 0.
    """
    probability = 0.5 + (power_attacker + stealth_factor - power_defender) / 20
    if random.random() < probability:
        return True
    return False

def randomize_draw(power_attacker, power_defender):
    """
    Default probability of a draw is 0.5, 
    it is then reduced by the sum of fighting hero powers in percents.
    If combined powers reach 50, a draw is no longer an option.
    """
    probability = 0.5 - (power_attacker + power_defender) / 100
    if random.random() < probability:
        return True
    return False


def get_hero_id_from_name(hero_name):
    """
    Gets hero id given hero's name.
    Intended mainly for use inside other functions.
    """

    # using first here bothers me
    hero = session.query(Hero).filter(Hero.name==hero_name).first()
    return hero.id


def hero_exists(id):
    """
    Checks if hero exists given hero id.
    Intended mainly for use inside other functions.
    """

    if session.query(Hero).get(id):
        return True
    return False


def add_hero(side, name, birthday, race, power):
    """
    Adds hero to database (table Hero)
    """

    birthday = datetime.date.fromisoformat(birthday)

    hero_to_add = Hero(side=side, name=name, 
                       birthday=birthday, race=race, power=power)
    session.add(hero_to_add)
    session.commit()
    logging.info("Added hero %s" % name)


def add_slogan(moto, hero_name):
    """
    Adds slogan of a given hero to the Slogan table.
    One hero can have multiple slogans.
    Indexing is independent for each hero and is done authomatically
    Each hero must have at least one slogan (not implemented yet).
    """

    hero_id = get_hero_id_from_name(hero_name)

    if not hero_exists(hero_id):
        logging.error("No such hero exists!")

    moto_id = session.query(Slogan.hero_id).filter(hero_id == hero_id).count() + 1

    slogan_to_add = Slogan(moto=moto, moto_id=moto_id, hero_id=hero_id)
    session.add(slogan_to_add)
    session.commit()
    logging.info("A brand new slogan for hero %s added successfully" %hero_name)


def add_backstory(story, hero_name):
    """
    Adds backstory of a given hero to the BackStory table.
    One hero can only have one backstory.
    If a backstory already exists for this hero, a warning will appear in stdout and log file.
    Backstory will be replaced but former backstory can be retrieved from log.txt
    """

    hero_id = get_hero_id_from_name(hero_name)
        
    if not hero_exists(hero_id):
        logging.error("No such hero exists!")
        return
    
    #replacing an exisisng story (using first() is probably a dirty hack)
    existing_backstory = session.query(BackStory).filter(BackStory.hero_id==hero_id).first()
    
    if existing_backstory:
        logging.warning("Backstory %s already exists for hero %s, replacing..." 
                        % (existing_backstory.story, hero_name))
        session.execute(update(BackStory).where(BackStory.hero_id == hero_id).values(story = story))
        session.commit()
        return   

    #adding a new story    
    story_to_add = BackStory(story=story, hero_id=hero_id)
    session.add(story_to_add)
    session.commit()
    logging.info("Backstory for hero %s added successfully" % hero_name)


def delete_hero(hero_name):
    """"
    Deletes a hero given hero's name.
    Hero's slogans and backstory are also deleted.
    """

    if hero_name not in (hero[0] for hero in session.query(Hero.name)):
        logging.error("No hero with name %s in database" % hero_name)
        
    session.execute(delete(Hero).where(Hero.name == hero_name))
    session.commit()
    
    logging.info("Hero %s deleted from database" % hero_name)


def add_confrontation(hero_1_id, hero_2_id, moto1, moto2, \
    attacker_index=random.choice([1, 2]), stealth_factor=2):
    """
    Adds a confrontation to the confrontation table.
    Optional parameter attacker_index determines who attacked first, 
    otherwise the attacker is chosen randomly.
    Attacker gets a stealth bonus that can be specified and defaults to 2.

    Fighting mechanics are implemented in the randomize_draw() and randomize_attack_success() functions.
    """
    
    hero1 = session.query(Hero).get(hero_1_id)
    hero2 = session.query(Hero).get(hero_2_id)

    #check  affiliations
    if hero1.side == hero2.side:
        logging.error("Heroes from the same side can't fight each other!!!")
        return
    
    #assign roles - attacker and defender
    if attacker_index == 1:
        attacker, defender = hero1, hero2
    else:
        attacker, defender = hero2, hero1

    # Find if ended in a draw
    if randomize_draw(attacker.power, defender.power):
        confrontation.insert().values(hero_1_id=attacker.id, hero_2_id=defender.id, \
            hero_1_moto_id=moto1, hero_2_moto_id=moto2, winner=0)

        result_message = f"{attacker.name} attacked {defender.name}. It ended in a draw."
        logging.info(result_message)
        return
    # Find if attacker won
    elif randomize_attack_success(attacker.power, defender.power, stealth_factor):
        winner = attacker
        loser = defender
        confrontation.insert().values(hero_1_id=attacker.id, hero_2_id=defender.id, \
            hero_1_moto_id=moto1, hero_2_moto_id=moto2,  winner=1)
    # None of the above happened => defender won
    else:
        winner = defender
        loser = attacker
        confrontation.insert().values(hero_1_id=attacker.id, hero_2_id=defender.id, \
            hero_1_moto_id=moto1, hero_2_moto_id=moto2, winner=2)
        
    result_message = f"{attacker.name} attacked {defender.name}. {winner.name} won!"
    logging.info(result_message)

    delete_hero(loser.name)


def pick_random_hero_id(side):
    """
    Pick random hero id.
    Used when creating a random confrontation.
    """
    all_hero_ids = []
    for hero in session.query(Hero).filter(Hero.side==side):
         all_hero_ids.append(hero.id)

    return random.choice(all_hero_ids)


def pick_random_moto_id(hero_id):
    """
    Pick random slogan id.
    Used when creating a random confrontation.
    """
    all_moto_ids = []
    for slogan in session.query(Slogan).filter(Slogan.hero_id==hero_id):
         all_moto_ids.append(slogan.moto_id)

    return random.choice(all_moto_ids)


def add_random_confrontation():
    """
    A wrapper for the add_confrontation function.
    Randomizes everything and then calls add_confrontation()
    """
    
    #get distinct sides and pick two at random
    all_sides = []
    for side in session.query(Hero.side).distinct():
        all_sides.append(side[0])
    
    #That implies only one side is left
    if  len(all_sides) < 2:
        winner = all_sides[0]
        logging.critical("There is only one side left! %s WON!" % winner)
        return

    fight_sides = random.sample(all_sides, 2)
    
    #pick heroes at random
    hero1_id = pick_random_hero_id(fight_sides[0])
    hero2_id = pick_random_hero_id(fight_sides[1])
    
    #pick motos at random for each hero
    moto1_id = pick_random_moto_id(hero1_id)
    moto2_id = pick_random_moto_id(hero2_id)
    
    #call the actual confrontation function
    add_confrontation(hero1_id, hero2_id, moto1_id, moto2_id)