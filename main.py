from organizer import MediaOrganizer
from file_scanner import FileScanner
from categorizer import Categorizer
from config import ConfigManager
from file_mover import FileMover

import argparse


def main():
    # Parsing args
    parser = argparse.ArgumentParser()

    parser.add_argument("--source", required=True)
    parser.add_argument("--destination", required=True)

    args = parser.parse_args()

    # Set up classes
    config = ConfigManager("config.json").load_config()

    scanner = FileScanner(args.source)
    categorizer = Categorizer(config)
    mover = FileMover(args.destination)

    # Start organizing
    organizer = MediaOrganizer(scanner, categorizer, mover)

    organizer.organize()


if __name__ == "__main__":
    main()
