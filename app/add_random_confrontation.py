import argparse
from data_interaction import add_random_confrontation

def main():
    parser = argparse.ArgumentParser(description="Command line argument parser for add_random_confrontation")
    parser.add_argument("number_of_fights", help="How many fights to add",
                        type=int)
    args = parser.parse_args()
    for i in range(args.number_of_fights):
        add_random_confrontation()

if __name__ == "__main__":
    main()