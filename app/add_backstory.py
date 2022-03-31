import argparse

from data_interaction import add_backstory


def main():
    parser = argparse.ArgumentParser(description="Command line argument parser for add_backstory()")
    parser.add_argument("story", help="The backstory you want to add",
                        type=str)
    parser.add_argument("hero_name", help="Name of the hero whose backstory you want to add",
                        type=str)
    args = parser.parse_args()

    add_backstory(args.story, args.hero_name)

if __name__ == "__main__":
    main()