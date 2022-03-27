import logging

#most logs with their time and function of origin will be stored in log.txt
logging.basicConfig(
    format="%(asctime)s => %(funcName)s => %(levelname)s => %(message)s",
    filename="log.txt",
    datefmt = "%Y-%m-%d %I:%M:%S",
    level=logging.INFO)

#most important logs will be printed to the console and seen right away!
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter("%(levelname)s => %(message)s")
console_handler.setFormatter(console_formatter)
logging.getLogger("").addHandler(console_handler)