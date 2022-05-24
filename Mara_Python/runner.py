from Mara import Mara as Mara_baby
from os import getenv
from logger import set_log


def start_bot():
    """Starts running Mara."""
    set_log()
    Mara = Mara_baby(getenv('TOKEN'))


def main():
    """Sets the log for Mara and starts running them."""
    set_log()
    start_bot()

if __name__ == '__main__':
    main()
