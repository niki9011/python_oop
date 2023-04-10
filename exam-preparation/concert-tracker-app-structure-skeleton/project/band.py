from typing import List

from project.band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Musician] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def __str__(self):
        number_of_members = len(self.members)
        return f"{self.name} with {number_of_members} members."
