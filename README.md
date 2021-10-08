# Nornir Napalm Netbox Demo

This repo contains 2 simple usecase that demo the integration of Netbox, Napalm and Nornir.

The full write up can be located at:
https://www.packetflow.co.uk/how-to-build-a-network-automation-stack-with-nornir-napalm-and-netbox/

## Layout

```
.
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
    ├ create_interfaces.py
    └ update_interfaces.py
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

Within `scripts/` you will find `helpers.py`. This contains the transform functions for manipulating the Nornir inventory, along with a small CLI, which contans some common actions that can help with dev/troubleshooting.

```
# scripts/helpers.py --help
usage: helpers.py [-h] [-i] [-n]

Nornir Helper CLI

optional arguments:
  -h, --help       show this help message and exit
  -i, --inventory  show inventory
  -n, --netbox     netbox debug
```

Note: When running the netbox option, use `python -i`, this will then drop into a shell, from which you will have access to the `netbox` instance.
