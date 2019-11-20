#!./venv/bin/python

import re
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir import InitNornir
from netbox import NetBox
from helpers import get_device_id, is_interface_present
import pprint

nr = InitNornir(config_file="./config.yaml")

nb_url, nb_token, ssl_verify = nr.config.inventory.options.values()
nb_host = re.sub("^.*//|:.*$", "", nb_url)

netbox = NetBox(host=nb_host, port=32768, use_ssl=False, auth_token=nb_token)
nb_interfaces = netbox.dcim.get_interfaces()


def create_netbox_interface(task, nb_interfaces, netbox):
    r = task.run(task=networking.napalm_get, getters=["interfaces"])
    interfaces = r.result["interfaces"]

    for interface_name in interfaces.keys():
        if not is_interface_present(nb_interfaces, f"{task.host}", interface_name):
            print(
                f"* Creating Netbox Interface for device {task.host}, interface {interface_name}"
            )
             device_id = get_device_id(f"{task.host}", netbox)
             netbox.dcim.create_interface(
                name=f"{interface_name}",
                form_factor=1200,  # default
                device_id=device_id,
             )


devices = nr.filter(role="switch")

result = devices.run(
    name="Create Netbox Interfaces",
    nb_interfaces=nb_interfaces,
    netbox=netbox,
    task=create_netbox_interface,
)
print_result(result, vars=["stdout"])
