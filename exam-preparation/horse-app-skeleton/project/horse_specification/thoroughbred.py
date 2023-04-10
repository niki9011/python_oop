from python_oop.FINAL_EXAM.project import Horse

class Thoroughbred(Horse):

    MAX_SPEED = 140
    SPEED_ADD = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = self.MAX_SPEED if self.speed + self.SPEED_ADD > self.MAX_SPEED else self.speed + self.SPEED_ADD


