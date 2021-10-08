from nornir import InitNornir
from nornir.core.plugins.inventory import TransformFunctionRegister
from secrets import creds
import re

def adapt_user_password(host):
    host.username = creds[f"{host}"]["username"]
    host.password = creds[f"{host}"]["password"]


TransformFunctionRegister.register("populate_creds", adapt_user_password)


nr = InitNornir(
        runner={
            "plugin": "threaded",
            "options": {
                "num_workers": 100,
            }
        },
        inventory={
            "plugin": "NetBoxInventory2",
            "options": {
                'nb_url': 'http://0.0.0.0:8000/',
                "nb_token": '0123456789abcdef0123456789abcdef01234567',
                "ssl_verify": False,
            },
            "transform_function": "populate_creds",    
        }
    )

nb_url, nb_token, ssl_verify = nr.config.inventory.options.values()
nb_host, nb_port = re.findall(".+?//(\S+):(\d+)", nb_url)[0]