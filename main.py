#!/usr/bin/env python3
import sys
import json
import re

assert sys.version_info >= (3, 8), "This script requires at least Python 3.8"

f = open("game.json")
data = json.load(f)
currentID = int(data["startnode"])


def getCurrent():
    return data["passages"][currentID-1]


def setCurrent(option):
    global currentID
    for x in data["passages"]:
        if x["name"].lower() == option:
            currentID = int(x["pid"])
            return True
    return False


def formatter(desc):
    desc = desc.replace("[[", "[")
    desc = re.sub("->.+?]", "", desc)
    return desc


while True:
    print("\n---\n")
    current = getCurrent()
    print(formatter(current["text"]))
    choice = input("What would you like to do? (\"quit\" to quit): ").lower()
    if choice == "quit":
        print("Thanks for playing!")
        break
    for x in current["links"]:
        if choice == x["name"].lower():
            setCurrent(x["link"].lower())
            break
