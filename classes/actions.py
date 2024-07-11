from abc import ABC, abstractmethod


class Action(ABC):
    @abstractmethod
    def act(self):
        """Execute an action on the system-under-test"""
        pass


class Verify(ABC):
    @abstractmethod
    def verify(self):
        """Execute a verification action on the system-under-test"""
        pass