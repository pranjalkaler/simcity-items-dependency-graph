class Node:
    def __init__(self, type, name, category, time=None):
        self.type = type
        self.name = name
        self.category = category
        self.time_to_build = time
        self.dependencies = dict()

    def requires(self, dependency, quantity):
        self.dependencies[dependency] = quantity

    def to_dict(self):
        return {
            "name": self.name,
            "type": f"{self.type}",
            "timeToBuild": self.time_to_build,
            "dependencies": {key.name: value for key, value in self.dependencies.items()}
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())