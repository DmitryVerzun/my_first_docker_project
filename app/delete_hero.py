import argparse

from data_interaction import delete_hero


def main():
    parser = argparse.ArgumentParser(description="Command line argument parser for delete_hero()")
    parser.add_argument("hero_name", help="Name of the hero you want deleted",
                        type=str)
    args = parser.parse_args()

    delete_hero(args.hero_name)

if __name__ == "__main__":
    main()
