[#!./venv/bin/python

import re
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir import InitNornir
from netbox import NetBox
import pprint

nr = InitNornir(config_file="./config.yaml")

nb_url, nb_token, ssl_verify = nr.config.inventory.options.values()
nb_host = re.sub("^.*//|:.*$", "", nb_url)

netbox = NetBox(host=nb_host, port=32768, use_ssl=False, auth_token=nb_token)
interfaces = netbox.dcim.get_interfaces()

def is_interface_present(interfaces, device_name, interface_name):
    print(device_name, interface_name)
    if [
        i
        for i in interfaces(device=device_name)
        if i["name"] == interface_name and i["device"]["display_name"] == device_name
    ]:
        print("yes")
        return True
    else:
        return False


def update_netbox_device_field(task):
    r = task.run(task=networking.napalm_get, getters=["interfaces"])
    interfaces = r.result["interfaces"]
    for interface_key in interfaces.keys():
        mac_address = interfaces[interface_key]["mac_address"]
        description = interfaces[interface_key]["description"]
        if is_interface_present(f"{task.host}", interface_key):
            netbox.dcim.update_interface(
                device=f"{task.host}",
                interface=interface_key,
                description=description,
                mac_address=mac_address,
            )


devices = nr.filter(role="switch")

result = devices.run(name="Update Netbox Interfaces", task=update_netbox_device_field)
print_result(result, vars=["stdout"])
