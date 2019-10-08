from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir import InitNornir

nr = InitNornir(config_file="./config.yaml")

cmh_spines = nr.filter(site="cmh")
result = cmh_spines.run(task=networking.napalm_get,
                        getters=["facts"])
print_result(result)
