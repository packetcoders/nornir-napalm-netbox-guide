#!/usr/bin/env python

from helpers import nornir_setup
from rich import print as rprint

nr = nornir_setup()

rprint(nr.inventory.dict())
