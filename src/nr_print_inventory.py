#!/usr/bin/env python

from rich import print as rprint

from helpers import nornir_setup

nr = nornir_setup()

inventory = nr.inventory.dict()

if __name__ == "__main__":
    rprint(inventory)
