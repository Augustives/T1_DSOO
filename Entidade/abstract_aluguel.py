from abc import ABC, abstractmethod
from datetime import date as Date

class AbstractAluguel(ABC):


@abstractmethod
def __init__(self, pessoa: Pessoa, quadra: Quadra, data_hora: str):
# https://stackabuse.com/converting-strings-to-datetime-in-python/


