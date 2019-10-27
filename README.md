## About
This repo contains 2 simple usecase that demo the integration of Netbox, Napalm and Nornir.

## Layout
```
.
├ config.yaml
├ data
│   └ configs
├ Makefile
├ README.md
├ requirements.txt
└ scripts
    ├ backup_configs.py
    ├ helpers.py
    ├ __init__.py
    ├ secrets.py
    └ update_netbox.py
```
## Files
* `Makefile` - various bash commands to set up environment.
* `secrets.py` - contains device username/passwords.
* `helpers.py` - contains inventory transform functions.
* `config.yaml` - nornir configuration inc. netbox plugin.

## Usecases
* Backup configs - `scripts/backup_configs.py`
* Populating Netbox - `scripts/update_netbox.py`

## Misc
### helpers.py
Within `scripts/` you will find `helpers.py`. This contains the transform functions for manipulating the Nornir inventory, along with a small CLI, which contans some common actions that can help with dev/troubleshooting..
```
usage: helpers.py [-h] [-i]

Nornir Helper CLI

optional arguments:
  -h, --help       show this help message and exit
  -i, --inventory  show inventory
```
