#!./venv/bin/python

import re
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir import InitNornir
from netbox import NetBox

nr = InitNornir(config_file="./config.yaml")

nb_url, nb_token, ssl_verify = nr.config.inventory.options.values()
nb_host = re.sub("^.*//|:.*$", "", nb_url)

netbox = NetBox(host=nb_host, port=32768, use_ssl=False, auth_token=nb_token)


def update_netbox_device_field(task):
    r = task.run(task=networking.napalm_get, getters=["facts"])
    os_version = r.result["facts"]["os_version"]
    netbox.dcim.update_device(
        device_name=f"{task.host}", custom_fields={"nos_version": os_version}
    )


devices = nr.filter()

result = devices.run(
    name="Update Netbox Device Version", task=update_netbox_device_field
)
print_result(result)
