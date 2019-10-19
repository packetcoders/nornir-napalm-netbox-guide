from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file
from nornir import InitNornir
from pprint import pprint

nr = InitNornir(config_file="./config.yaml")

print(nr.inventory.hosts.keys)
print(nr.inventory.groups)
print("======================")
from nornir.core.deserializer.inventory import InventoryElement
import json
print(json.dumps(InventoryElement.schema(), indent=4))
print("======================")
pprint(nr.inventory.get_hosts_dict())
