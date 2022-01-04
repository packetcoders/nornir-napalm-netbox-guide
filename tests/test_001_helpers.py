import os
import sys

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/src")

from helpers import nornir_setup


def test_nr_setup():
    nr = nornir_setup()
    assert type(nr.inventory.defaults.username) == str
    assert type(nr.inventory.defaults.password) == str
    assert nr.config.inventory.plugin == "NetBoxInventory2"
