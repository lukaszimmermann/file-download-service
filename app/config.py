"""
Provides access to the app config
"""
import os
from util import fatal_if


def get_config_files_dir():
    config_files_dir = "CONFIG_FILES_DIR"
    fatal_if(config_files_dir not in os.environ, 'Config Key: \'CONFIG_FILES_DIR\' not found in environment', 1)
    return os.environ[config_files_dir]
