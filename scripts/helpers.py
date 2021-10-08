#!./venv/bin/python

from secrets import creds
from rich import print
from netbox import NetBox
import argparse
import re
from rich import print
import __init__

# Tranform Functions

def is_interface_present(nb_interfaces, device_name, interface_name):
    for i in nb_interfaces:
        if i["name"] == interface_name and i["device"]["display_name"] == device_name:
            return True
    return False


def get_device_id(device_name, netbox):
    device_id = netbox.dcim.get_devices(name=device_name)[0]["id"]
    return device_id


# CLI

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nornir Helper CLI")
    parser.add_argument("-i", "--inventory", action="store_true", help="show inventory", required=False)
    parser.add_argument("-n", "--netbox", action="store_true", help="netbox debug", required=False)

    args = vars(parser.parse_args())
    if args["inventory"]:
        print(__init__.nr.inventory.dict())
    elif args["netbox"]:
        # to be used with python -i
        netbox = NetBox(host=__init__.nb_host, port=__init__.nb_port, use_ssl=False, auth_token=__init__.nb_token)