from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file
from nornir import InitNornir


nr = InitNornir(config_file="./config.yaml")

print(nr.inventory.hosts)
print(nr.inventory.groups)

