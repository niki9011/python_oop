from python_oop.FINAL_EXAM.project import Appaloosa
from python_oop.FINAL_EXAM.project import Thoroughbred


class HorseRaceApp:
    HORSE_BREEDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred,}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_race = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSE_BREEDS:
            self.horses.append(self.HORSE_BREEDS[horse_type](horse_name, horse_speed))

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        if jockey_name in self.jockeys:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        else:
            self.jockeys.append(jockey_name)
            return f"Jockey {jockey_name} is added."


    def create_horse_race(self, race_type: str):
        if race_type in self.horse_race:
            raise Exception("Race {race type} has been already created!")

        else:
            self.horse_race.append(race_type)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))

        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass



horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))
