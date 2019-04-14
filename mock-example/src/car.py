"""A class representing a car, with a dependency on an engine"""

class Car:
    """A car that can be turned off and can be inspected"""
    def __init__(self, engine):
        self.engine = engine

    def is_on(self):
        return self.engine.on

    def turn_off(self):
        return self.engine.turn_off()
