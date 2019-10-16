from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file
from nornir import InitNornir

BACKUP_PATH = "./data/configs"


def backup_config(task, path):
    r = task.run(task=networking.napalm_get, getters=["config"])
    task.run(
        task=write_file,
        content=r.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )


nr = InitNornir(config_file="./config.yaml")

devices = nr.filter(site="cmh")

result = devices.run(
    name="Backup device configurations", path=BACKUP_PATH, task=backup_config
)
print_result(result, vars=["stdout"])
