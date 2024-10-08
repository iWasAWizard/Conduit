#!/bin/python

import configparser
import json
import importlib

def get_config(config_path="./config.ini"):
    config = configparser.ConfigParser()
    config.read(f"{config_path}")

    return config

def get_module_list(config_path="./config.ini"):
    module_list = json.loads(config["modules"])

    return module_list

def import_modules(module_list):
    for m in module_list:
        importlib.import_module(f"modules.{m}")
