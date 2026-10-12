from location import *

class Entity(Location):

    locations = Location.__get__()

    def __init__(self, name, description, nature, type, categorie, state, location, date):
        super.__init__(name, description, nature, type, categorie, state)
        self.state = state
        self.location = location


    @classmethod
    def __new__(cls, locations):

        name = input("Enter a name :")
        description = input("Enter a description :")
        nature= input("Select nature")
        type = input("Select type")
        categorie = input("Select type")
        location = locations[4]
        return cls(name, description, nature, type, categorie, location)


class Situation(Entity):

    def __init__(self, id, name, description, location, state, date, presents):
        super.__init__(id, name, description, location,  state, date)
        self.presents = presents












