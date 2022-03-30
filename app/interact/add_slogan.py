import argparse

from data_interaction import add_slogan


def main():
    parser = argparse.ArgumentParser(description="Command line argument parser for add_slogan()")
    parser.add_argument("moto", help="The slogan you want to add",
                        type=str)
    parser.add_argument("hero_name", help="Name of you hero",
                        type=str)
    args = parser.parse_args()

    add_slogan(args.moto, args.hero_name)


if __name__ == "__main__":
    main()
