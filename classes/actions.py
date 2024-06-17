from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def act(self):
        """Execute an action on the system-under-test"""
        pass
