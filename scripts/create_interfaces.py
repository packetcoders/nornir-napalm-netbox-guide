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


def create_netbox_interface(task, nb_interfaces, netbox):
    r = task.run(task=napalm_get, getters=["interfaces"])
    interfaces = r.result["interfaces"]

    for interface_name in interfaces.keys():
        if not is_interface_present(nb_interfaces, f"{task.host}", interface_name):
            print(
                f"* Creating Netbox Interface for device {task.host}, interface {interface_name}"
            )
            device_id = get_device_id(f"{task.host}", netbox)
            netbox.dcim.create_interface(
                name=f"{interface_name}",
                device_id=device_id,
                interface_type="1000base-t",
            )


result = __init__.nr.run(
    name="Create Netbox Interfaces",
    nb_interfaces=nb_interfaces,
    netbox=netbox,
    task=create_netbox_interface,
)
print_result(result, vars=["stdout"])
