#!/usr/bin/env python3

from Database import DatabaseInterface
from time import sleep

def main():
    db = DatabaseInterface("riddell.dev")

    db.log_soil(90, "strawberries", 1)
    sleep(1)
    db.log_soil(80, "strawberries", 1)
    sleep(1)
    db.log_soil(70, "strawberries", 1)
    sleep(1)
    db.log_soil(60, "strawberries", 1)
    sleep(1)
    db.log_soil(50, "strawberries", 1)

if __name__ == "__main__":
    main()