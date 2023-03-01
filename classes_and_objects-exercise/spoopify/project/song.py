class Song:
    def __init__(self, name: str, lenght: float, single: bool):
        self.name = name
        self.lenght = lenght
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.lenght}"
