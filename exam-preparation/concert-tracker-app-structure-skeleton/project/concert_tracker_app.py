from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int) -> str:

        VALID_MUSICIANS = {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer}

        if musician_type not in VALID_MUSICIANS.keys():
            raise ValueError("Invalid musician type!")

        names = [musician.name for musician in self.musicians]
        
        if name in names:
            raise Exception(f"{name} is already a musician!")

        new_musician = VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        names = [band.name for band in self.bands]
        if name in names:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:

        concert = [c for c in self.concerts if c.place == place]

        if concert:
            concert = concert[0]
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        # If there isn't a band with the given name, raise an Exception
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        # If there isn't a musician with the given name who is a member of the given band, raise an Exception
        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [m for m in band.members if isinstance(m, Singer)]
        drummers = [m for m in band.members if isinstance(m, Drummer)]
        guitarists = [m for m in band.members if isinstance(m, Guitarist)]

        if not (singers and drummers and guitarists):
            raise Exception(f"{band} can't start the concert because it doesn't have enough members!")

        are_singers_qualified = True

        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    are_singers_qualified = False
            elif concert.genre == "Metal":
                if "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False
            else:
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False

        are_drummer_qualified = True

        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummer_qualified = False
            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummer_qualified = False
            else:
                if "play the drums with drum brushes" not in drummer.skills:
                    are_drummer_qualified = False

        are_guitarist_qualified = True

        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    are_guitarist_qualified = False
            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    are_guitarist_qualified = False
            else:
                if "play jazz" not in guitarist.skills:
                    are_guitarist_qualified = False

        if not are_drummer_qualified or not are_guitarist_qualified or not are_singers_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."