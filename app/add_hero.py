import argparse
import datetime

from data_interaction import add_hero


def main():
    parser = argparse.ArgumentParser(description="Command line argument parser for add_hero()")

    parser.add_argument("side", help="The side your hero is on",
                        type=str)
    parser.add_argument("name", help="Your hero's name",
                        type=str)
    parser.add_argument("birthday", help="Your hero's birthday (must be in yyyy-mm-dd format)",
                        type=str)
    parser.add_argument("race", help="Your hero's race",
                        type=str)
    parser.add_argument("power", help="Your hero's power level (look into Readme for details)",
                        type=int)
    args = parser.parse_args()

    add_hero(args.side, args.name, args.birthday, args.race, args.power) 

if __name__ == "__main__":
    main()