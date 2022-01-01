import os
import sys

import pytest

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/src")

from nr_backup_configs import result


@pytest.mark.parametrize("device", list(result.keys()))
def test_backup_configs_get_config(device):
    assert not result[device][1].failed


@pytest.mark.parametrize("device", list(result.keys()))
def test_backup_configs_write_file(device):
    assert not result[device][2].failed
