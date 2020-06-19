import json
import os.path

from .path import relative


CONFIG_FILENAME = 'config.json'


def _get_config_fp():
    if os.path.exists(relative(CONFIG_FILENAME)):
        return open(relative(CONFIG_FILENAME))
    
    with open(relative(CONFIG_FILENAME), 'w') as f:
        f.write('{}')

    return _get_config_fp()


class VVCConfig(dict):
    def __init__(self):
        super().__init__(
                json.load(_get_config_fp()))

    def save(self):
        json.dump(self, open(relative(CONFIG_FILENAME), 'w'))

    def __setitem__(self, key :str, value :str):
        super().__setitem__(key, value)
        self.save()


CONFIG = VVCConfig()
