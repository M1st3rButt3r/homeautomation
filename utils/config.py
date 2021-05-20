import json
from os.path import join

import utils.files

with open(join(utils.files.get_root_path(), "config.json")) as json_file:
    config = json.load(json_file)
