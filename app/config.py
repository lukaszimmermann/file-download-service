"""
Provides access to the app config
"""
import os
from util import fatal_if


def get_config_files_dir():
    config_files_dir = "CONFIG_FILES_DIR"
    fatal_if(config_files_dir not in os.environ, 'Config Key: \'CONFIG_FILES_DIR\' not found in environment', 1)
    return os.environ[config_files_dir]


def get_config_default_file():
    config_default_file = "CONFIG_DEFAULT_FILE"
    if config_default_file in os.environ:
        return os.environ[config_default_file]
    return None

