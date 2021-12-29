#!./venv/bin/python

import os
from pathlib import Path

from dotenv import load_dotenv
from nornir import InitNornir

load_dotenv()

NORNIR_CONFIG_FILE = f"{Path(__file__).parent.parent}/config.yaml"


def nornir_setup():
    nr = InitNornir(config_file=NORNIR_CONFIG_FILE)

    nr.inventory.defaults.username = os.getenv("DEVICE_USERNAME")
    nr.inventory.defaults.password = os.getenv("DEVICE_PASSWORD")

    return nr
