from abc import ABC, abstractmethod

class Verify(ABC):
    @abstractmethod
    def verify(self):
        """ Verify state of system-under-test"""
        pass
