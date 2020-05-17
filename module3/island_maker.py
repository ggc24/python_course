from escape_unicode import escape_unicode
from tracer import tracer

@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'

class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix

