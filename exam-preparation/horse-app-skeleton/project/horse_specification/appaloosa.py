from python_oop.FINAL_EXAM.project import Horse


class Appaloosa(Horse):

    MAX_SPEED = 120
    SPEED_ADD = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)


    def train(self):
        self.speed = self.MAX_SPEED if self.speed + self.SPEED_ADD > self.MAX_SPEED else self.speed + self.SPEED_ADD
