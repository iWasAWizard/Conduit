#!/bin/python
from abc import ABC, abstractmethod


class Endpoint(ABC):
    def __init__(self, hostname:str , username:str, password:str):
        self.hostname = hostname
        self.username = username
        self.password = password

        self.platform = "idk, probably linux"