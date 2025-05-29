from abc import ABC, abstractmethod

class LogReader(ABC):
    @abstractmethod
    def read_logs(self):
        pass