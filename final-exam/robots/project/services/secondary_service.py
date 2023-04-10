from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name, capacity=15):
        super().__init__(name, capacity)

    def details(self):
        result = [f"{self.name} Secondary Service:"]
        robots = "none"

        if len(self.robots) > 0:
            robots = ' '.join([robot.name for robot in self.robots])

        result.append(f"Robots: {robots}")

        return '\n'.join(result)