#!./venv/bin/python

from helpers import nornir_setup
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file

nr = nornir_setup()

BACKUP_PATH = "./data/configs"


def backup_config(task, path):
    r = task.run(task=napalm_get, getters=["config"])
    task.run(
        task=write_file,
        content=r.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )


result = nr.run(
    name="Backup Device configurations", path=BACKUP_PATH, task=backup_config
)

print_result(result, vars=["stdout"])
