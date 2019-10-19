#!./venv/bin/python

from secrets import creds


def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]


if __name__ == "__main__":
    from nornir import InitNornir
    from pprint import pprint
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Nornir Helper CLI")
    parser.add_argument(
        "-i", "--inventory", action="store_true", help="inventory", required=False
    )

    args = vars(parser.parse_args())

    if args["inventory"]:
        nr = InitNornir(config_file="./config.yaml")
        pprint(nr.inventory.get_inventory_dict())
