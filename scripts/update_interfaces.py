#!./venv/bin/python

import re
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_napalm.plugins.tasks import napalm_get
from netbox import NetBox
from helpers import get_device_id, is_interface_present
from rich import print
import __init__

netbox = NetBox(
    host=__init__.nb_host,
    port=__init__.nb_port,
    use_ssl=False,
    auth_token=__init__.nb_token,
)
nb_interfaces = netbox.dcim.get_interfaces()


def update_netbox_interface(task, nb_interfaces):
    r = task.run(task=napalm_get, getters=["interfaces"])
    interfaces = r.result["interfaces"]

    for interface_name in interfaces.keys():
        mac_address = interfaces[interface_name]["mac_address"]
        if mac_address == "None" or mac_address == "Unspecified":
            mac_address = "ee:ee:ee:ee:ee:ee"

        description = interfaces[interface_name]["description"]

        if is_interface_present(nb_interfaces, f"{task.host}", interface_name):
            print(f"* Updating Netbox Interface for device {task.host}, interface {interface_name}")
            netbox.dcim.update_interface(
                device=f"{task.host}",
                interface=interface_name,
                description=description,
                mac_address=mac_address,
            )

result = __init__.nr.run(
    name="Update Netbox Interfaces",
    nb_interfaces=nb_interfaces,
    task=update_netbox_interface,
)
print_result(result, vars=["stdout"])
