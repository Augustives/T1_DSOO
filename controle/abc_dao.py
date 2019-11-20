import pickle
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource=""):
        self.datasource = datasource
        self.objectcache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.objectcache, open(self.datasource, 'wb'))

    def __load(self):
        self.objectcache = pickle.load(open(self.datasource, 'rb'))


    def add(self, key, obj):
        self.objectcache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.objectcache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.objectcache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.objectcache.values()
