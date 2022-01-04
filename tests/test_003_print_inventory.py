import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/src")

from nr_print_inventory import inventory


@pytest.fixture
def inventory_keys():
    return ["hosts", "groups", "defaults"]


def test_print_inventory(inventory_keys):
    assert list(inventory.keys()) == inventory_keys
