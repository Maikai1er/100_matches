class Matches:
    def __init__(self):
        self.matches = 100

    def pull_matches(self, *, count: int):
        self.matches -= count