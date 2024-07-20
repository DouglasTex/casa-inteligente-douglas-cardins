from abc import abstractmethod, ABC


class Dispositivo(ABC):

    @abstractmethod
    def status_atual(self):
        ...
