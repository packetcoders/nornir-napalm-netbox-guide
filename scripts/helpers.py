#!./venv/bin/python

from secrets import creds
from nornir import InitNornir
from pprint import pprint
from netbox import NetBox
import argparse
import json
import re

# Tranform Functions


def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]


# Netbox


nr = InitNornir(config_file="./config.yaml")

nb_url, nb_token, ssl_verify = nr.config.inventory.options.values()
nb_host = re.sub("^.*//|:.*$", "", nb_url)


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
        # to be used with python -i
        netbox = NetBox(host=nb_host, port=32768, use_ssl=False, auth_token=nb_token)
