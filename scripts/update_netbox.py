#!./venv/bin/python

from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file
from nornir import InitNornir
from netbox import NetBox
import re

nr = InitNornir(config_file="./config.yaml")

NB_URL, NB_TOKEN, SSL_VERIFY = nr.config.inventory.options.values()
NB_HOST = re.sub("^.*//|:.*$", "", NB_URL)

NETBOX = NetBox(host=NB_HOST, port=32768, use_ssl=False, auth_token=NB_TOKEN)


def update_netbox_device_field(task):
    r = task.run(task=networking.napalm_get, getters=["facts"])
    os_version = r.result["facts"]["os_version"]
    NETBOX.dcim.update_device(
        device_name=f"{task.host}", custom_fields={"nos_version": os_version}
    )


nr = InitNornir(config_file="./config.yaml")

devices = nr.filter()

result = devices.run(
    name="Update Netbox Device Version", task=update_netbox_device_field
)
print_result(result)
