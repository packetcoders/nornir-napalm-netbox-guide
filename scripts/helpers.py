#!./venv/bin/python -i

from secrets import creds
from nornir import InitNornir
from pprint import pprint
from netbox import NetBox
import argparse
import json

# Tranform Functions


def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]


# Netbox


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
    parser.add_argument(
        "-i", "--inventory", action="store_true", help="show inventory", required=False
    )
    parser.add_argument(
        "-n", "--netbox", action="store_true", help="netbox debug", required=False
    )

    args = vars(parser.parse_args())

    if args["inventory"]:
        nr = InitNornir(config_file="./config.yaml")
        pprint(nr.inventory.get_inventory_dict())
    elif args["netbox"]:
        netbox = NetBox(
            host="172.29.236.139",
            port=32768,
            use_ssl=False,
            auth_token="c6d10bb5a03e11120719b2a704409b4a4a7bd004",
        )
